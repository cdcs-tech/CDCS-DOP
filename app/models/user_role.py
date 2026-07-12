"""
CDCS Digital Operations Platform (CDCS-DOP)

User Role Association Model

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.3 – User Role Assignment Foundation
"""

from app.extensions import db


user_roles = db.Table(
    "user_roles",

    db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey("users.id"),
        primary_key=True
    ),

    db.Column(
        "role_id",
        db.Integer,
        db.ForeignKey("roles.id"),
        primary_key=True
    )
)