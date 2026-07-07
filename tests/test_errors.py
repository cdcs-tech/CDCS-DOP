import pytest

def test_404_page(client):
    response = client.get("/page-that-does-not-exist")

    assert response.status_code == 404


@pytest.mark.skip(reason="403 route will be implemented during Authentication (Milestone 2)")
def test_403_page(client):
    pass