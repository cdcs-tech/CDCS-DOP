"""
CDCS Digital Operations Platform (CDCS-DOP)

User Service

Provides business logic for user management.
"""

from app.extensions import db
from app.models.user import User
from app.services.base_service import BaseService


class UserService(BaseService):
    """
    Business logic for user management.
    """

    @staticmethod
    def create_user(
        full_name,
        email,
        password,
        role="Staff",
        is_active=True,
    ):
        """
        Create a new user account.

        Returns:
            tuple(bool, str, User | None)
            (success, message, user)
        """

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            return (
                False,
                "A user with this email already exists.",
                None,
            )

        user = User(
            full_name=full_name,
            email=email,
            role=role,
            is_active=is_active,
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return (
            True,
            "User created successfully.",
            user,
        )