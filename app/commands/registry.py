"""
CDCS Digital Operations Platform (CDCS-DOP)

Command Registry

Registers all enterprise command groups with
the Flask application.
"""

from app.commands.admin import admin_cli


def register_commands(app):
    """
    Register all CLI command groups.

    Args:
        app:
            Flask application instance.
    """

    app.cli.add_command(admin_cli)