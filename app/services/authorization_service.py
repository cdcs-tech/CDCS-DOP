"""
CDCS Digital Operations Platform (CDCS-DOP)

Authorization Service

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.4 – Authorization Service Layer
"""

from app.extensions import db
from app.models.permission import Permission
from app.models.role import Role
from app.models.user import User


class AuthorizationService:
    """
    Central service for RBAC operations.
    """

    # ----------------------------------------------------
    # User ↔ Role Operations
    # ----------------------------------------------------

    @staticmethod
    def assign_role(user: User, role: Role) -> bool:
        """
        Assign a role to a user.
        """

        if role not in user.roles:
            user.roles.append(role)
            db.session.commit()

        return True

    @staticmethod
    def remove_role(user: User, role: Role) -> bool:
        """
        Remove a role from a user.
        """

        if role in user.roles:
            user.roles.remove(role)
            db.session.commit()

        return True

    @staticmethod
    def user_has_role(user: User, role_name: str) -> bool:
        """
        Determine whether a user has the specified role.
        """

        return any(
            role.name == role_name
            for role in user.roles
        )

    # ----------------------------------------------------
    # Role ↔ Permission Operations
    # ----------------------------------------------------

    @staticmethod
    def grant_permission(role: Role, permission: Permission) -> bool:
        """
        Grant a permission to a role.
        """

        if permission not in role.permissions:
            role.permissions.append(permission)
            db.session.commit()

        return True

    @staticmethod
    def revoke_permission(role: Role, permission: Permission) -> bool:
        """
        Remove a permission from a role.
        """

        if permission in role.permissions:
            role.permissions.remove(permission)
            db.session.commit()

        return True

    # ----------------------------------------------------
    # Authorization
    # ----------------------------------------------------

    @staticmethod
    def user_has_permission(user: User, permission_name: str) -> bool:
        """
        Determine whether a user has the specified permission.
        """

        for role in user.roles:
            for permission in role.permissions:

                if permission.name == permission_name:
                    return True

        return False