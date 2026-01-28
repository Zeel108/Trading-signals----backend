import uuid

def create_user_and_login(client):
    email = f"user_{uuid.uuid4()}@test.com"
    password = "test1234"

    client.post("/auth/signup", json={
        "email": email,
        "password": password
    })

    res = client.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert res.status_code == 200
    assert "access_token" in res.json()

    return res.json()["access_token"]
