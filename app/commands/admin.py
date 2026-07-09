"""
CDCS Digital Operations Platform (CDCS-DOP)

Administrator Commands
"""

import click


@click.group(name="admin")
def admin_cli():
    """
    Administrator management commands.
    """
    pass