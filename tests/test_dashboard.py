def test_dashboard_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"CDCS Digital Operations Platform" in response.data