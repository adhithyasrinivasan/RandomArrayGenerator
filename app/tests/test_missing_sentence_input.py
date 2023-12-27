from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    response = client.post("/random_array_generator/token")
    print(response)
    return response.json()["access_token"]

def test_missing_sentence_field():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/random_array_generator", json={},headers=headers)
    assert response.status_code == 422  # Unprocessable Entity