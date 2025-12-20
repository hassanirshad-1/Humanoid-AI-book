from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_chat_endpoint():
    """Test the chat POST endpoint with streaming response."""
    payload = {
        "message": "What is a robot?",
        "context": {"session_id": "test_session", "current_url": "/chapter-01-intro"}
    }
    with client.stream("POST", "/chat", json=payload) as response:
        assert response.status_code == 200
        assert response.headers["content-type"] == "text/event-stream"
        
        # Read at least one chunk to verify it's working
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                assert "type" in data
                assert data["type"] in ["data", "error", "end"]
                break

def test_chat_missing_context():
    """Test chat endpoint with minimal payload."""
    payload = {"message": "Hi"}
    with client.stream("POST", "/chat", json=payload) as response:
        assert response.status_code == 200

def test_options_chat():
    """Test OPTIONS request for CORS preflight."""
    response = client.options("/chat")
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
