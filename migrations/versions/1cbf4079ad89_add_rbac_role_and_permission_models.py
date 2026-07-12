"""Add RBAC role and permission models

Revision ID: 1cbf4079ad89
Revises: 02fdee9c07dc
Create Date: 2026-07-10 23:49:53.835858

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1cbf4079ad89"
down_revision = "02fdee9c07dc"
branch_labels = None
depends_on = None


def upgrade():

    # Permissions table
    op.create_table(
        "permissions",

        sa.Column(
            "name",
            sa.String(length=120),
            nullable=False
        ),

        sa.Column(
            "description",
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            "module",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "action",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),

        sa.UniqueConstraint(
            "name"
        )
    )


    # Roles table
    op.create_table(
        "roles",

        sa.Column(
            "name",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "description",
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),

        sa.UniqueConstraint(
            "name"
        )
    )


    # Role-Permission association table
    op.create_table(
        "role_permissions",

        sa.Column(
            "role_id",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "permission_id",
            sa.Integer(),
            nullable=False
        ),

        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permissions.id"]
        ),

        sa.ForeignKeyConstraint(
            ["role_id"],
            ["roles.id"]
        ),

        sa.PrimaryKeyConstraint(
            "role_id",
            "permission_id"
        )
    )


def downgrade():

    op.drop_table(
        "role_permissions"
    )

    op.drop_table(
        "roles"
    )

    op.drop_table(
        "permissions"
    )