"""
CDCS Digital Operations Platform (CDCS-DOP)
Application Extensions

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.2 – Flask-Login Integration
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
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    """
    Temporary user loader.

    The actual implementation will be completed in
    Package 2.2 when the User model is introduced.
    """
    return None