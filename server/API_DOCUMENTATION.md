# API Documentation

## Endpoints

### Start Session

- **URL:** `/api/v1/chat/start_session`
- **Method:** `POST`
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Session created",
    "data": {
      "session_id": "uuid-string"
    }
  }
  ```

### Create Message

- **URL:** `/api/v1/chat/create_message`
- **Method:** `POST`
- **Headers:** 
  - Cookie: `session_id=uuid-string`
- **Request Body:**
  ```json
  {
    "content": "Your message here"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Message sent successfully",
    "data": [
      {
        "id": 1,
        "session_id": "uuid-string",
        "content": "Your message here",
        "is_from_user": true,
        "created_at": "2023-07-30T12:34:56.789Z",
        "updated_at": "2023-07-30T12:34:56.789Z"
      },
      {
        "id": 2,
        "session_id": "uuid-string",
        "content": "Bot response here",
        "is_from_user": false,
        "created_at": "2023-07-30T12:34:57.789Z",
        "updated_at": "2023-07-30T12:34:57.789Z"
      }
    ]
  }
  ```

### Edit Message

- **URL:** `/api/v1/chat/edit_message/{message_id}`
- **Method:** `PATCH`
- **Headers:** 
  - Cookie: `session_id=uuid-string`
- **Request Body:**
  ```json
  {
    "content": "Updated message content"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Message updated",
    "data": {
      "id": 1,
      "session_id": "uuid-string",
      "content": "Updated message content",
      "is_from_user": true,
      "created_at": "2023-07-30T12:34:56.789Z",
      "updated_at": "2023-07-30T12:35:56.789Z"
    }
  }
  ```

### Delete Message

- **URL:** `/api/v1/chat/delete_message/{message_id}`
- **Method:** `DELETE`
- **Headers:** 
  - Cookie: `session_id=uuid-string`
- **Response:**
  ```json
  {
    "status": "success",
    "message": "Message deleted successfully"
  }
  ```

## Error Responses

All endpoints may return the following error response:

```json
{
  "status": "error",
  "message": "Error description here"
}
```

Common error scenarios:
- 401 Unauthorized: No active session or invalid session
- 404 Not Found: Message not found
- 400 Bad Request: Invalid input data