def test_register(client, db_session):
    res = client.post("/users/register", json={
        "username": "john",
        "email": "john@example.com",
        "password": "1234"
    })
    assert res.status_code == 200

def test_login(client, db_session):
    res = client.post("/users/login", json={
        "username": "john",
        "password": "1234"
    })
    assert res.status_code == 200
