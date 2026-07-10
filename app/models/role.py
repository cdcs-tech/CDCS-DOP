"""
CDCS Digital Operations Platform (CDCS-DOP)

Role Model

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.2 – Permission Model Foundation
"""

from app.extensions import db
from app.models.base import BaseModel


role_permissions = db.Table(
    "role_permissions",

    db.Column(
        "role_id",
        db.Integer,
        db.ForeignKey("roles.id"),
        primary_key=True
    ),

    db.Column(
        "permission_id",
        db.Integer,
        db.ForeignKey("permissions.id"),
        primary_key=True
    )
)


class Role(BaseModel):
    """
    System roles.

    Roles group permissions
    assigned to users.
    """

    __tablename__ = "roles"


    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )


    description = db.Column(
        db.String(255),
        nullable=True
    )


    permissions = db.relationship(
        "Permission",
        secondary=role_permissions,
        backref="roles"
    )


    def __repr__(self):
        return f"<Role {self.name}>"