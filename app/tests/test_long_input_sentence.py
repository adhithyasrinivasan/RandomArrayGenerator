from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    response = client.post("/random_array_generator/token")
    print(response)
    return response.json()["access_token"]

def test_long_sentence():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/random_array_generator", json={"sentence": "A" * 2000},headers=headers)
    assert response.status_code == 422
    print(response.json())
    assert "ensure this value has at most 1000 characters" in response.json()['detail'][0]['msg']