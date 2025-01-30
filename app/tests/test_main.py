from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
STATUS_CODE_200 = 200
STATUS_CODE_422 = 422


def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == STATUS_CODE_200
    assert response.json() == {"message": "Welcome to the Essay Generator API!"}


def test_generate_essay() -> None:
    response = client.get("/essay?topic=AI")
    assert response.status_code == STATUS_CODE_200

    response = client.get("/essay")
    assert response.status_code == STATUS_CODE_422
