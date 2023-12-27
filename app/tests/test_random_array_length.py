from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    response = client.post("/random_array_generator/token")
    print(response)
    return response.json()["access_token"]

def test_array_length():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/random_array_generator", json={"sentence": "This is a valid sentence."},headers=headers)
    assert response.status_code == 200
    np_array = response.json()['random_array']
    assert len(np_array)==500