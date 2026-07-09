"""
CDCS Digital Operations Platform (CDCS-DOP)

Administrator Commands

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.4.2 – Administrator Command Group
"""

import click

from app.extensions import db
from app.models.user import User


@click.group(name="admin")
def admin_cli():
    """
    Administrator management commands.
    """
    pass


@admin_cli.command("create")
def create_admin():
    """
    Create the initial system administrator.
    """

    click.echo()
    click.echo("=" * 60)
    click.echo("CDCS Digital Operations Platform")
    click.echo("Administrator Account Creation")
    click.echo("=" * 60)
    click.echo()

    full_name = click.prompt(
        "Full Name",
        type=str
    ).strip()

    email = click.prompt(
        "Email Address",
        type=str
    ).strip().lower()

    existing = User.query.filter_by(
        email=email
    ).first()

    if existing:

        click.secho(
            "\nAn account with this email already exists.",
            fg="red"
        )

        return

    while True:

        password = click.prompt(
            "Password",
            hide_input=True,
            confirmation_prompt=True
        )

        if len(password) < 8:

            click.secho(
                "\nPassword must contain at least 8 characters.",
                fg="yellow"
            )

            continue

        break

    role = click.prompt(
        "Role",
        default="Administrator",
        show_default=True
    )

    user = User(
        full_name=full_name,
        email=email,
        role=role,
        is_active=True
    )

    user.set_password(password)

    try:

        db.session.add(user)
        db.session.commit()

        click.echo()

        click.secho(
            "Administrator account created successfully.",
            fg="green"
        )

        click.echo(f"Name : {user.full_name}")
        click.echo(f"Email: {user.email}")
        click.echo(f"Role : {user.role}")

        click.echo()

    except Exception as exc:

        db.session.rollback()

        click.secho(
            f"\nError creating administrator: {exc}",
            fg="red"
        )