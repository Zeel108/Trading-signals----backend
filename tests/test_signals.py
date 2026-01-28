from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token():
    res = client.post("/auth/login", json={
        "email": "testuser@gmail.com",
        "password": "test1234"
    })
    return res.json()["access_token"]