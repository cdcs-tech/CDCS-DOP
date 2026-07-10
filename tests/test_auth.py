"""
CDCS Digital Operations Platform (CDCS-DOP)

Authentication Tests

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.5.4 – Authentication Redirect Testing
"""

import pytest

from app.models.user import User
from app.extensions import db


@pytest.fixture
def admin_user(app):
    """
    Create a test administrator.
    """

    with app.app_context():

        user = User(
            full_name="Test Administrator",
            email="admin@test.local",
            role="Administrator",
            is_active=True,
        )

        user.set_password("Password123!")

        db.session.add(user)
        db.session.commit()

        yield user

        db.session.delete(user)
        db.session.commit()


def login(client):
    """
    Authenticate the test administrator.
    """

    return client.post(
        "/auth/login",
        data={
            "email": "admin@test.local",
            "password": "Password123!",
            "remember": False,
        },
        follow_redirects=True,
    )


def logout(client):
    """
    Log out the authenticated user.
    """

    return client.get(
        "/auth/logout",
        follow_redirects=True,
    )


def test_dashboard_requires_login(client):
    """
    AUTH-001

    Anonymous users should be redirected
    to the login page.
    """

    response = client.get("/", follow_redirects=False)

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_system_requires_login(client):
    """
    AUTH-002
    """

    response = client.get("/system", follow_redirects=False)

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_health_is_public(client):
    """
    AUTH-003
    """

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] in ["Healthy", "Warning"]


def test_valid_login(client, admin_user):
    """
    AUTH-004
    """

    response = login(client)

    assert response.status_code == 200

    assert b"Career Development" in response.data


def test_invalid_login(client):
    """
    AUTH-005
    """

    response = client.post(
        "/auth/login",
        data={
            "email": "unknown@test.local",
            "password": "WrongPassword",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert b"Invalid email or password." in response.data


def test_logout(client, admin_user):
    """
    AUTH-006
    """

    login(client)

    response = logout(client)

    assert response.status_code == 200

    assert b"You have been logged out successfully." in response.data


def test_dashboard_after_logout(client, admin_user):
    """
    AUTH-007
    """

    login(client)

    logout(client)

    response = client.get("/", follow_redirects=False)

    assert response.status_code == 302

    assert "/auth/login" in response.headers["Location"]


def test_system_after_logout(client, admin_user):
    """
    AUTH-008
    """

    login(client)

    logout(client)

    response = client.get("/system", follow_redirects=False)

    assert response.status_code == 302

    assert "/auth/login" in response.headers["Location"]