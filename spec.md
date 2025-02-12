# Wisdom API Specification

## Overview

The **Wisdom API** provides real-time access to structured data insights via a WebSocket-based subscription model. Users can ask questions related to business intelligence and receive structured responses, including tabular data and SQL queries.

## Authentication

The API requires authentication using a **session token** obtained via the Descope authentication system.

### Authentication Flow

1. **Obtain Session Token**

   - Use the `exchange_access_key` method from Descope to exchange an access key for a session token.
   - Python Example:
     ```python
     from descope import DescopeClient
     descope_client = DescopeClient(project_id=WISDOM_PROJECT_ID)
     auth_info = descope_client.exchange_access_key(WISDOM_AUTH_KEY)
     auth_token = auth_info["sessionToken"]["jwt"]
     ```

2. **Pass Token in Requests**

   - The session token is required in the WebSocket connection payload and query parameters.

## WebSocket Connection

### Connection URL

```
wss://<WISDOM_WS_URL>
```

### Connection Parameters

| Parameter    | Type   | Description                          |
| ------------ | ------ | ------------------------------------ |
| `auth.token` | String | JWT session token for authentication |

Example:

```json
{
  "auth": {
    "token": "<SESSION_TOKEN>"
  }
}
```

## Subscription Request

To query the API, subscribe to the `chat` GraphQL subscription with the following parameters.

### Subscription Endpoint

```graphql
subscription Chat(
    $auth: SubscriptionAuthInput!,
    $conversationId: String,
    $domainId: String!,
    $query: StructuredQuery!,
    $idempotencyKey: String!,
    $toolSelection: ToolSelection
) {
    chat(
        auth: $auth,
        conversationId: $conversationId,
        domainId: $domainId,
        query: $query,
        idempotencyKey: $idempotencyKey,
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
```

### Request Parameters

| Parameter        | Type            | Required | Description                                           |
| ---------------- | --------------- | -------- | ----------------------------------------------------- |
| `auth`           | Object          | ✅        | Authentication token payload                          |
| `conversationId` | String          | ❌        | ID of an existing conversation for context continuity |
| `domainId`       | String          | ✅        | Domain ID to scope the query                          |
| `query`          | StructuredQuery | ✅        | Query input object                                    |
| `idempotencyKey` | String          | ✅        | Unique key to prevent duplicate requests              |
| `toolSelection`  | ToolSelection   | ❌        | Specifies enabled tools for the query                 |

### Example Subscription Request

```json
{
  "auth": { "token": "<SESSION_TOKEN>" },
  "domainId": "<DOMAIN_ID>",
  "query": { "pieces": [ { "text": "What is the expected revenue from each opportunity?" } ] },
  "idempotencyKey": "12345678",
  "toolSelection": { "optInToolNames": ["Tabular Data"] }
}
```

## Response Structure

### Success Response

```json
{
  "chat": {
    "messageId": "msg_12345",
    "bodyDiff": {
      "ops": [
        {
          "insert": {
            "text": "Let me fetch a table for expected revenue for each opportunity."
          }
        },
        {
          "insert": {
            "visualization": {
              "title": "Revenue by Opportunity",
              "data": [
                { "value": "Company A", "hyperlink": null },
                { "value": "$20,000", "hyperlink": null }
              ],
              "columns": [
                { "name": "Opportunity" },
                { "name": "Revenue" }
              ],
              "code": {
                "codeStr": "SELECT opportunity, revenue FROM sales_data;",
                "dialect": "SQL"
              }
            }
          }
        }
      ]
    },
    "conversationId": "conv_98765",
    "inProgress": false
  }
}
```

### Response Fields

| Field            | Type    | Description                                         |
| ---------------- | ------- | --------------------------------------------------- |
| `messageId`      | String  | Unique message identifier                           |
| `bodyDiff.ops`   | Array   | List of response operations (text or visualization) |
| `inProgress`     | Boolean | Whether the query is still processing               |
| `conversationId` | String  | Conversation ID for session tracking                |

## Error Handling

| Error Code | Message               | Cause                                   |
| ---------- | --------------------- | --------------------------------------- |
| `401`      | Unauthorized          | Invalid or missing authentication token |
| `400`      | Bad Request           | Malformed request payload               |
| `500`      | Internal Server Error | Unexpected API failure                  |

## Contact & Support

For any queries or support, contact our API team at [**support@askwisdom.ai**](mailto\:support@askwisdom.ai).

---

© 2025 Wisdom API. All rights reserved.

