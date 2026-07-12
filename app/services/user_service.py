"""
CDCS Digital Operations Platform (CDCS-DOP)

User Management Service Layer

Milestone 2 – Authentication & Security
Package 2.3 – User Management
Stage 2.3.4 – User Management Service Layer
"""

from werkzeug.security import generate_password_hash

from app.extensions import db
from app.models.user import User
from app.models.role import Role


class UserService:
    """
    Handles administrative user management operations.
    """


    @staticmethod
    def create_user(
        full_name,
        email,
        password,
    ):
        """
        Create a new user account.
        """

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            raise ValueError(
                "User with this email already exists."
            )


        user = User(
            full_name=full_name,
            email=email,
            password_hash=generate_password_hash(password),
            is_active=True
        )


        db.session.add(user)
        db.session.commit()


        return user



    @staticmethod
    def get_users():
        """
        Return all users.
        """

        return User.query.all()



    @staticmethod
    def get_user_by_id(user_id):
        """
        Return user by ID.
        """

        return User.query.get(user_id)



    @staticmethod
    def update_user(
        user,
        full_name=None,
        email=None
    ):
        """
        Update user information.
        """

        if full_name:
            user.full_name = full_name


        if email:
            user.email = email


        db.session.commit()

        return user



    @staticmethod
    def activate_user(user):
        """
        Activate user account.
        """

        user.is_active = True

        db.session.commit()

        return user



    @staticmethod
    def deactivate_user(user):
        """
        Deactivate user account.
        """

        user.is_active = False

        db.session.commit()

        return user



    @staticmethod
    def assign_role(user, role_name):
        """
        Assign role to user.
        """

        role = Role.query.filter_by(
            name=role_name
        ).first()


        if not role:
            raise ValueError(
                "Role does not exist."
            )


        if role not in user.roles:

            user.roles.append(role)

            db.session.commit()


        return user



    @staticmethod
    def remove_role(user, role_name):
        """
        Remove role from user.
        """

        role = Role.query.filter_by(
            name=role_name
        ).first()


        if role and role in user.roles:

            user.roles.remove(role)

            db.session.commit()


        return user