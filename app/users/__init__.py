"""
CDCS Digital Operations Platform (CDCS-DOP)

User Management Blueprint

Milestone 2 – Authentication & Security
Package 2.3 – User Administration
Stage 2.3.2 – User Management Module Foundation
"""

from flask import Blueprint

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)

from app.users import routes