from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

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
