from fastapi.testclient import TestClient
from main import app
from app.users import current_active_user
from app.models import User
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

def test_translate_endpoint():
    """Test the translation POST endpoint."""
    response = client.post(
        "/api/translate",
        json={"text": "Hello, how are you?", "target_language": "Urdu"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert "source_language" in data

def test_translate_empty_text():
    """Test translation with empty text (should fail validation)."""
    response = client.post(
        "/api/translate",
        json={"text": "", "target_language": "Urdu"}
    )
    assert response.status_code == 422 # Pydantic validation error

def test_translate_missing_payload():
    """Test translation with missing payload."""
    response = client.post("/api/translate", json={})
    assert response.status_code == 422
