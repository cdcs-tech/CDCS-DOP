"""
CDCS Digital Operations Platform (CDCS-DOP)

Dashboard Authentication Tests

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.5.6 – Package Testing & Release
"""

from app.models.user import User
from app.extensions import db


def create_test_user():
    """
    Create an authenticated test user.
    """

    user = User(
        full_name="Test Administrator",
        email="admin@test.com",
        role="Administrator",
        is_active=True,
    )

    user.set_password("Password123")

    db.session.add(user)
    db.session.commit()

    return user



def login_test_user(client):
    """
    Authenticate a test user.
    """

    create_test_user()

    return client.post(
        "/auth/login",
        data={
            "email": "admin@test.com",
            "password": "Password123",
        },
        follow_redirects=True,
    )



def test_dashboard_requires_login(client):
    """
    Anonymous users should be redirected
    to the login page.
    """

    response = client.get(
        "/",
        follow_redirects=False
    )

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]



def test_dashboard_home_authenticated(client):
    """
    Authenticated users should access
    the enterprise dashboard.
    """

    login_test_user(client)

    response = client.get("/")

    assert response.status_code == 200
    assert b"CDCS Digital Operations Platform" in response.data