from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Essay Generator API!"}

def test_generate_essay():
    response = client.get("/essay?topic=AI")
    assert response.status_code == 200
    assert response.json() == {"topic": "AI", "essay": "This is an essay on AI"}

    response = client.get("/essay")
    assert response.status_code == 422
