"""
CDCS Digital Operations Platform (CDCS-DOP)

User Model

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.3 – User Model Foundation
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.base import BaseModel
from app.models.user_role import user_roles


class User(BaseModel, UserMixin):
    """
    System users.

    Provides authentication support through Flask-Login
    and secure password management.
    """

    __tablename__ = "users"

    roles = db.relationship(
    "Role",
    secondary=user_roles,
    backref="users"
    )

    # ----------------------------------------------------
    # User Information
    # ----------------------------------------------------

    full_name = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    # ----------------------------------------------------
    # Authentication
    # ----------------------------------------------------

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    # ----------------------------------------------------
    # Authorization Foundation
    # ----------------------------------------------------

    role = db.Column(
        db.String(50),
        default="Staff"
    )

    # ----------------------------------------------------
    # Account Status
    # ----------------------------------------------------

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    # ----------------------------------------------------
    # Password Management
    # ----------------------------------------------------

    def set_password(self, password):
        """
        Generate and store a secure password hash.

        Plain text passwords should never be stored.
        """

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify a supplied password against the stored hash.
        """

        return check_password_hash(
            self.password_hash,
            password
        )

    # ----------------------------------------------------
    # Representation
    # ----------------------------------------------------

    def __repr__(self):
        return f"<User {self.email}>"