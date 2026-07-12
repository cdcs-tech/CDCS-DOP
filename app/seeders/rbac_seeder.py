"""
CDCS Digital Operations Platform (CDCS-DOP)

RBAC Seeder

Creates default roles and permissions.

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
"""

from app.extensions import db

from app.models.role import Role
from app.models.permission import Permission


def seed_rbac():
    """
    Create default roles and permissions.
    """

    # -------------------------------------------------
    # Permissions
    # -------------------------------------------------

    permissions = [
        {
            "name": "users.view",
            "module": "Users",
            "action": "View",
            "description": "View system users"
        },
        {
            "name": "users.create",
            "module": "Users",
            "action": "Create",
            "description": "Create new users"
        },
        {
            "name": "users.update",
            "module": "Users",
            "action": "Update",
            "description": "Update user information"
        },
        {
            "name": "users.assign_role",
            "module": "Users",
            "action": "Assign Role",
            "description": "Assign roles to users"
        },
        {
            "name": "system.manage",
            "module": "System",
            "action": "Manage",
            "description": "Manage system configuration"
        },
    ]


    created_permissions = {}

    for item in permissions:

        permission = Permission.query.filter_by(
            name=item["name"]
        ).first()

        if not permission:

            permission = Permission(**item)

            db.session.add(permission)

        created_permissions[item["name"]] = permission


    db.session.commit()


    # -------------------------------------------------
    # Roles
    # -------------------------------------------------

    administrator = Role.query.filter_by(
        name="Administrator"
    ).first()


    if not administrator:

        administrator = Role(
            name="Administrator",
            description="Full system administrator"
        )

        db.session.add(administrator)

        db.session.commit()


    # -------------------------------------------------
    # Assign permissions
    # -------------------------------------------------

    administrator.permissions = list(
        created_permissions.values()
    )

    db.session.commit()


    print("RBAC seeding completed successfully.")