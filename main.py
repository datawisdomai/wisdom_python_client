import os
from dotenv import load_dotenv
import asyncio
from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport
import pandas as pd
import sqlparse
from descope import (
    DescopeClient,
)

# Load environment variables from .env file
# Make sure to write the env variables in the .env file
load_dotenv()

# Get environment variables
WISDOM_WS_URL = os.getenv("wisdom_ws_url")
WISDOM_AUTH_KEY = os.getenv("wisdom_auth_key")
WISDOM_PROJECT_ID = os.getenv("wisdom_project_id")
DOMAIN_ID = os.getenv("domain_id")

if not WISDOM_WS_URL:
    raise ValueError("wisdom_ws_url is not set")
if not DOMAIN_ID:
    raise ValueError("domain_id is not set")
if not WISDOM_PROJECT_ID:
    raise ValueError("wisdom_project_id is not set")
if not WISDOM_AUTH_KEY:
    raise ValueError("wisdom_auth_key is not set")

descope_client = DescopeClient(project_id=WISDOM_PROJECT_ID)

# Define the subscription query
CHAT_SUBSCRIPTION = gql(
    """
    subscription Chat(
        $auth: SubscriptionAuthInput!, 
        $conversationId: String, 
        $domainId: String!, 
        $query: StructuredQuery!, 
        $idempotencyKey: String!, 
        $toolSelection: ToolSelection
    ) {
        chat(
            auth: $auth
            conversationId: $conversationId
            domainId: $domainId
            query: $query
            idempotencyKey: $idempotencyKey
            toolSelection: $toolSelection
        ) {
            messageId
            bodyDiff {
                ops {
                    insert {
                        text
                        visualization {
                            id
                            title
                            type
                            dimensions
                            measures
                            measureGroups {
                                label
                                measures
                                format
                            }
                            data {
                                value
                                hyperlink
                            }
                            columns {
                                name
                                description
                                alias
                                uniqueRef
                                tableName
                            }
                            columnOrder
                            columnDisplayFormats
                            hasMore
                            pagination {
                                pageIndex
                                pageSize
                            }
                            code {
                                codeStr
                                dialect
                            }
                        }
                    }
                    retain
                    delete
                }
            }
            inProgress
            conversationId
            diffIndex
            createdAt
            updatedAt
            dataRefreshedAt
        }
    }
    """
)


def get_auth_token():
    """Get an auth token for the Wisdom API."""
    auth_info = descope_client.exchange_access_key(WISDOM_AUTH_KEY)
    return auth_info["sessionToken"]["jwt"]


async def ask_question(question: str) -> str:
    """
    Ask a question to the Wisdom API and yield streaming responses.

    Args:
        question: The question to ask

    Yields:
        Streaming responses from the API
    """
    auth_token = get_auth_token()

    if not WISDOM_WS_URL:
        raise ValueError("wisdom_ws_url is not set")

    # Separate connection auth from subscription variables
    connection_params = {"auth": {"token": auth_token}}

    subscription_variables = {
        "auth": {"token": auth_token},
        "domainId": DOMAIN_ID,
        "query": {
            "pieces": [
                {
                    "text": question,
                }
            ]
        },
        "idempotencyKey": str(hash(question)),
        "toolSelection": {"optInToolNames": ["Tabular Data"]},
    }
    # Set up the WebSocket transport with authentication
    transport = WebsocketsTransport(
        url=WISDOM_WS_URL,
        init_payload=connection_params,
    )

    response_obj = None

    async with Client(
        transport=transport,
        fetch_schema_from_transport=True,
    ) as session:
        async for result in session.subscribe(
            CHAT_SUBSCRIPTION, variable_values=subscription_variables
        ):
            if result.get("chat"):
                response_obj = result["chat"]

    response_text = ""
    for op in response_obj["bodyDiff"]["ops"]:
        if op.get("insert") and op["insert"].get("text"):
            response_text += op["insert"]["text"]
        elif op.get("insert") and op["insert"].get("visualization"):
            viz = op["insert"]["visualization"]
            data = viz["data"]
            data = [[cell.get("value") for cell in row] for row in data]

            columns = viz["columns"]
            column_names = [column["name"] for column in columns]
            df = pd.DataFrame(data, columns=column_names)
            response_text += "\n\n" + df.head().to_string() + "\n\n"

            sql = viz.get("code", {}).get("codeStr")
            if sql:
                # Format the SQL code with proper indentation and capitalization
                formatted_sql = sqlparse.format(
                    sql, reindent=True, keyword_case="upper"
                )
                response_text += "\n\n" + formatted_sql + "\n\n"

    return response_text


async def main():
    """Main function to run the Wisdom API."""
    # List of questions to ask
    questions = [
        "What is the expected revenue from each opportunity?",
        "List all opportunities",
    ]

    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}/{len(questions)}: {question}")
        print("Answer: ", end="", flush=True)
        response = await ask_question(question)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
