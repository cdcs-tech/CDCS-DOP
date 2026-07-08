"""
CDCS Digital Operations Platform (CDCS-DOP)
Authentication Blueprint

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.1 – Authentication Blueprint Creation
"""

from flask import Blueprint

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

from app.auth import routes