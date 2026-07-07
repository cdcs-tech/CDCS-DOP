def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] in ["Healthy", "Warning"]


def test_system_page(client):
    response = client.get("/system")

    assert response.status_code == 200