"""
CDCS Digital Operations Platform (CDCS-DOP)

Permission Seeder

Milestone 2 – Authentication & Security
Package 2.3 – User Management
Stage 2.3.3 – User Management Permission Foundation
"""

from app.extensions import db
from app.models.permission import Permission


USER_MANAGEMENT_PERMISSIONS = [

    {
        "name": "users.view",
        "module": "Users",
        "action": "View",
        "description": "View user accounts"
    },

    {
        "name": "users.create",
        "module": "Users",
        "action": "Create",
        "description": "Create new user accounts"
    },

    {
        "name": "users.update",
        "module": "Users",
        "action": "Update",
        "description": "Update existing user accounts"
    },

    {
        "name": "users.delete",
        "module": "Users",
        "action": "Delete",
        "description": "Delete or deactivate user accounts"
    },

    {
        "name": "roles.assign",
        "module": "Roles",
        "action": "Assign",
        "description": "Assign roles to users"
    }

]


def seed_user_permissions():

    created = 0

    for permission_data in USER_MANAGEMENT_PERMISSIONS:

        existing = Permission.query.filter_by(
            name=permission_data["name"]
        ).first()


        if not existing:

            permission = Permission(
                name=permission_data["name"],
                module=permission_data["module"],
                action=permission_data["action"],
                description=permission_data["description"]
            )

            db.session.add(permission)

            created += 1


    db.session.commit()

    return created