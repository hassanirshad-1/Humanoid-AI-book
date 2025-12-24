from fastapi.testclient import TestClient
from main import app
from app.users import current_active_user
from app.models import User
import json
import uuid

client = TestClient(app)

# Mock user for authentication bypass
mock_user = User(
    id=uuid.uuid4(),
    email="test@example.com",
    hashed_password="mock_hashed_password",
    is_active=True,
    is_superuser=False,
    is_verified=True,
    name="Test User",
    skill_level="Intermediate",
    operating_system="Linux"
)

def override_current_active_user():
    return mock_user

app.dependency_overrides[current_active_user] = override_current_active_user

def test_chat_endpoint():
    """Test the chat POST endpoint with streaming response."""
    payload = {
        "message": "What is a robot?",
        "context": {"session_id": "test_session", "current_url": "/chapter-01-intro"}
    }
    with client.stream("POST", "/chat", json=payload) as response:
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]
        
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
