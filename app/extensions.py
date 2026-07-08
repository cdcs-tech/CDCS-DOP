"""
CDCS Digital Operations Platform (CDCS-DOP)

Application Extensions

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.3 – User Model Foundation
"""

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# ----------------------------------------------------
# Database
# ----------------------------------------------------

db = SQLAlchemy()


# ----------------------------------------------------
# Database Migration
# ----------------------------------------------------

migrate = Migrate()


# ----------------------------------------------------
# Authentication
# ----------------------------------------------------

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.login_message = (
    "Please log in to access this page."
)

login_manager.login_message_category = "warning"

login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    """
    Load authenticated user from database.

    Flask-Login calls this function whenever it
    needs to restore a user session.

    Args:
        user_id:
            User primary key stored in session.

    Returns:
        User object or None.
    """

    from app.models.user import User

    return User.query.get(int(user_id))