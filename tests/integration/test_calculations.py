def test_create_calc(client, db_session):
    res = client.post("/calculations", json={
        "expression": "2+2",
        "result": 4
    })
    assert res.status_code == 200
    assert res.json()["result"] == 4
