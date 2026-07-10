"""
CDCS Digital Operations Platform (CDCS-DOP)

Permission Model

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.2 – Permission Model Foundation
"""

from app.extensions import db
from app.models.base import BaseModel


class Permission(BaseModel):
    """
    System permissions.

    Represents individual actions
    users can perform.
    """

    __tablename__ = "permissions"


    name = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )


    description = db.Column(
        db.String(255),
        nullable=True
    )


    module = db.Column(
        db.String(100),
        nullable=False
    )


    action = db.Column(
        db.String(100),
        nullable=False
    )


    def __repr__(self):
        return f"<Permission {self.name}>"