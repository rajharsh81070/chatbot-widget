from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_start_session():
    response = client.post("/api/v1/chat/start_session")
    assert response.status_code == 200
    assert "session_id" in response.json()["data"]


def test_send_message():
    session_response = client.post("/api/v1/chat/start_session")
    session_id = session_response.json()["data"]["session_id"]

    message_response = client.post(
        "/api/v1/chat/create_message",
        json={"content": "Hello"},
        cookies={"session_id": session_id}
    )
    assert message_response.status_code == 200
    assert len(message_response.json()["data"]) == 2
