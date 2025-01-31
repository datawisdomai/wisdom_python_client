import requests
import os
from dotenv import load_dotenv
import asyncio
from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport
from gql.transport.requests import RequestsHTTPTransport
from typing import AsyncGenerator, Optional

from descope import (
    REFRESH_SESSION_TOKEN_NAME,
    SESSION_TOKEN_NAME,
    AuthException,
    DeliveryMethod,
    DescopeClient,
    AssociatedTenant,
    RoleMapping,
    AttributeMapping,
)

# Load environment variables from .env file
load_dotenv()

# Get environment variables
WISDOM_API_URL = os.getenv("wisdom_api_url")
WISDOM_WS_URL = os.getenv("wisdom_ws_url")
WISDOM_AUTH_KEY = os.getenv("wisdom_auth_key")
WISDOM_PROJECT_ID = os.getenv("wisdom_project_id")

if not WISDOM_PROJECT_ID:
    raise ValueError("wisdom_project_id is not set")
if not WISDOM_AUTH_KEY:
    raise ValueError("wisdom_auth_key is not set")
if not WISDOM_API_URL:
    raise ValueError("wisdom_api_url is not set")

descope_client = DescopeClient(project_id=WISDOM_PROJECT_ID)

# Define the subscription query
CHAT_SUBSCRIPTION = gql(
    """
    subscription Chat($auth: SubscriptionAuthInput!, $conversationId: String, $createHiddenConversation: Boolean, $domainId: String!, $query: StructuredQuery!, $skipCompose: Boolean, $idempotencyKey: String!, $toolSelection: ToolSelection, $manualModelSelection: LLMModel) {
        chat(
            auth: $auth
            conversationId: $conversationId
            createHiddenConversation: $createHiddenConversation
            domainId: $domainId
            query: $query
            skipCompose: $skipCompose
            idempotencyKey: $idempotencyKey
            toolSelection: $toolSelection
            manualModelSelection: $manualModelSelection
        ) {
            text
            done
            error
        }
    }
"""
)


def get_auth_token():
    """Get an auth token for the Wisdom API."""
    auth_info = descope_client.exchange_access_key(WISDOM_AUTH_KEY)
    return auth_info["sessionToken"]["jwt"]


WISDOM_DOMAIN_ID = "ET_DOMAIN_9118ac9c9f424498831d1870534bd6f1"


async def ask_question(question: str) -> AsyncGenerator[str, None]:
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

    # Set up the WebSocket transport with authentication
    transport = WebsocketsTransport(
        url=WISDOM_WS_URL, headers={"Authorization": f"Bearer {auth_token}"}
    )

    async with Client(
        transport=transport,
        fetch_schema_from_transport=True,
    ) as session:
        # Prepare the variables for the subscription
        variables = {
            "auth": {"token": auth_token},
            "domainId": WISDOM_DOMAIN_ID,
            "query": {"text": question},
            "idempotencyKey": str(
                hash(question)
            ),  # Simple way to generate an idempotency key
        }

        try:
            async for result in session.subscribe(
                CHAT_SUBSCRIPTION, variable_values=variables
            ):
                if result.get("chat"):
                    message = result["chat"]
                    if message.get("error"):
                        yield f"Error: {message['error']}"
                        break
                    if message.get("text"):
                        yield message["text"]
                    if message.get("done"):
                        break
        except Exception as e:  # pylint: disable=broad-exception-caught
            yield f"Error during subscription: {str(e)}"


async def main():
    """Main function to run the Wisdom API."""
    # List of questions to ask
    questions = [
        "What is the meaning of life?",
        "How do I implement a binary search in Python?",
        "What is the airspeed velocity of an unladen swallow?",
    ]

    for question in questions:
        print(f"\nQuestion: {question}")
        print("Answer: ", end="", flush=True)
        async for response in ask_question(question):
            print(response, end="", flush=True)
        print()  # New line after complete response


if __name__ == "__main__":
    asyncio.run(main())
