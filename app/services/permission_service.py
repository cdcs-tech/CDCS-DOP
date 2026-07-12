"""
CDCS Digital Operations Platform (CDCS-DOP)

Permission Service

Milestone 2 – Authentication & Security
Package 2.3 – User Administration
Stage 2.3.3 – User Management Permission Foundation
"""

from app.extensions import db
from app.models.permission import Permission
from app.models.role import Role
from app.services.authorization_service import AuthorizationService


class PermissionService:
    """
    Centralized service responsible for registering
    and assigning application permissions.

    All application modules should register their
    permissions through this service.
    """

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
            "name": "users.edit",
            "module": "Users",
            "action": "Edit",
            "description": "Edit user accounts"
        },
        {
            "name": "users.delete",
            "module": "Users",
            "action": "Delete",
            "description": "Delete or archive user accounts"
        },
        {
            "name": "roles.assign",
            "module": "Roles",
            "action": "Assign",
            "description": "Assign and revoke user roles"
        }
    ]

    @staticmethod
    def register_permission(permission_data):
        """
        Register a permission if it does not already exist.
        """

        permission = Permission.query.filter_by(
            name=permission_data["name"]
        ).first()

        if permission:
            return permission

        permission = Permission(
            name=permission_data["name"],
            module=permission_data["module"],
            action=permission_data["action"],
            description=permission_data["description"]
        )

        db.session.add(permission)
        db.session.commit()

        return permission

    @classmethod
    def register_permissions(cls, permissions):
        """
        Register a collection of permissions.
        """

        registered = []

        for permission in permissions:
            registered.append(
                cls.register_permission(permission)
            )

        return registered

    @classmethod
    def bootstrap_user_permissions(cls):
        """
        Register all user management permissions.
        """

        return cls.register_permissions(
            cls.USER_MANAGEMENT_PERMISSIONS
        )

    @classmethod
    def assign_permissions_to_role(
        cls,
        role_name,
        permissions
    ):
        """
        Assign multiple permissions to a role.
        """

        role = Role.query.filter_by(
            name=role_name
        ).first()

        if role is None:
            raise ValueError(
                f"Role '{role_name}' does not exist."
            )

        for permission_name in permissions:

            permission = Permission.query.filter_by(
                name=permission_name
            ).first()

            if permission is None:
                raise ValueError(
                    f"Permission '{permission_name}' does not exist."
                )

            AuthorizationService.grant_permission(
                role,
                permission
            )

        db.session.commit()

        return role

    @classmethod
    def bootstrap_administrator_permissions(cls):
        """
        Register user-management permissions and
        assign them to the Administrator role.
        """

        cls.bootstrap_user_permissions()

        cls.assign_permissions_to_role(
            "Administrator",
            [
                "users.view",
                "users.create",
                "users.edit",
                "users.delete",
                "roles.assign"
            ]
        )