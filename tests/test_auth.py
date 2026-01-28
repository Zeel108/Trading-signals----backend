from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_signup():
    response = client.post("/auth/signup", json={
        "email": "testuser@gmail.com",
        "password": "test1234"
    })
    assert response.status_code in [200, 400]

def test_login():
    response = client.post("/auth/login", json={
        "email": "testuser@gmail.com",
        "password": "test1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
