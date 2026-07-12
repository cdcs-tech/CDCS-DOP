"""
CDCS Digital Operations Platform (CDCS-DOP)

System Route Tests

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
"""

from app.extensions import db
from app.models.permission import Permission
from app.models.role import Role
from app.models.user import User
from app.services.authorization_service import AuthorizationService


def login_system_admin(client):
    """
    Create and authenticate a system administrator
    with the required permission.
    """

    user = User.query.filter_by(
        email="system@test.com"
    ).first()

    if user is None:
        user = User(
            full_name="System Administrator",
            email="system@test.com",
            is_active=True
        )

        user.set_password("password123")

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

    client.post(
        "/auth/login",
        data={
            "email": "system@test.com",
            "password": "password123"
        },
        follow_redirects=True
    )


def test_health_endpoint(client):
    """
    Health endpoint remains public.
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
    Anonymous users are redirected
    to the login page.
    """

    response = client.get(
        "/system",
        follow_redirects=False
    )

    assert response.status_code == 302
    assert "/auth/login" in response.headers["Location"]


def test_system_page_authenticated(client, app):
    """
    Authenticated administrator with the required
    permission can access the system page.
    """

    with app.app_context():
        login_system_admin(client)

    response = client.get("/system")

    assert response.status_code == 200
    assert b"CDCS Digital Operations Platform" in response.data