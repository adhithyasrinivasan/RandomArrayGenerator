from fastapi.testclient import TestClient
from main import app
from app.api.random_generator import generate_random_array


client = TestClient(app)

def get_token():
    response = client.post("/random_array_generator/token")
    return response.json()["access_token"]

def test_valid_request():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/random_array_generator", json={"sentence": "This is a valid sentence."},headers=headers)
    assert response.status_code == 200
    assert "random_array" in response.json()
    
def test_generate_random_array():
    random_array=generate_random_array()
    assert isinstance(random_array, list)
    assert len(random_array) == 500