"""
CDCS Digital Operations Platform (CDCS-DOP)

RBAC Regression Tests

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.5.1 – RBAC Regression Testing
"""

import pytest

from app.extensions import db
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.services.authorization_service import AuthorizationService


@pytest.fixture
def admin_user(app):
    """
    Create administrator user with role and permission.
    """

    with app.app_context():

        user = User.query.filter_by(
            email="admin@test.com"
        ).first()

        if user is None:

            user = User(
                full_name="Administrator User",
                email="admin@test.com",
                is_active=True
            )

            user.set_password(
                "password123"
            )

            db.session.add(user)
            db.session.commit()


        role = Role.query.filter_by(
            name="Administrator"
        ).first()

        if role is None:

            role = Role(
                name="Administrator",
                description="System Administrator"
            )

            db.session.add(role)
            db.session.commit()


        permission = Permission.query.filter_by(
            name="system.manage"
        ).first()

        if permission is None:

            permission = Permission(
                name="system.manage",
                module="System",
                action="Manage",
                description="Manage system settings"
            )

            db.session.add(permission)
            db.session.commit()


        AuthorizationService.assign_role(
            user,
            role
        )

        AuthorizationService.grant_permission(
            role,
            permission
        )


        yield user


@pytest.fixture
def login_admin(client, admin_user):

    client.post(
        "/auth/login",
        data={
            "email": "admin@test.com",
            "password": "password123"
        },
        follow_redirects=True
    )

    return client


def test_anonymous_admin_route_requires_login(client):
    """
    Anonymous users cannot access admin-only route.
    """

    response = client.get(
        "/admin-only",
        follow_redirects=False
    )

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]



def test_admin_role_access(login_admin):
    """
    Administrator can access role protected route.
    """

    response = login_admin.get(
        "/admin-only"
    )

    assert response.status_code == 200
    assert (
        b"Administrator access granted"
        in response.data
    )



def test_admin_permission_access(login_admin):
    """
    Administrator can access permission protected route.
    """

    response = login_admin.get(
        "/system"
    )

    assert response.status_code == 200



def test_authenticated_user_without_permission(
    client,
    app
):
    """
    User without RBAC permission receives 403.
    """

    with app.app_context():

        user = User(
            full_name="Normal User",
            email="user@test.com",
            is_active=True
        )

        user.set_password(
            "password123"
        )

        db.session.add(user)
        db.session.commit()


    client.post(
        "/auth/login",
        data={
            "email": "user@test.com",
            "password": "password123"
        },
        follow_redirects=True
    )

    response = client.get(
        "/system"
    )

    assert response.status_code == 403