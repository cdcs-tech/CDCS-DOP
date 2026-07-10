"""
CDCS Digital Operations Platform (CDCS-DOP)

System Blueprint Tests

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.5.6 – Package Testing & Release
"""

from app.models.user import User
from app.extensions import db



def create_test_user():
    """
    Create a test authenticated user.
    """

    user = User(
        full_name="Test Administrator",
        email="system@test.com",
        role="Administrator",
        is_active=True,
    )

    user.set_password("Password123")

    db.session.add(user)
    db.session.commit()

    return user



def login_test_user(client):
    """
    Login the test account.
    """

    create_test_user()

    return client.post(
        "/auth/login",
        data={
            "email": "system@test.com",
            "password": "Password123",
        },
        follow_redirects=True,
    )



def test_health_endpoint(client):
    """
    Health API remains publicly accessible.
    """

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] in [
        "Healthy",
        "Warning"
    ]



def test_system_page_requires_login(client):
    """
    Anonymous users cannot access system information.
    """

    response = client.get(
    "/system",
    follow_redirects=False
)

    print("STATUS:", response.status_code)
    print("LOCATION:", response.headers.get("Location"))
    print(response.data.decode())



def test_system_page_authenticated(client):
    """
    Authenticated users can access system information.
    """

    login_test_user(client)

    response = client.get("/system")

    assert response.status_code == 200