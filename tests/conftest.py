"""
CDCS Digital Operations Platform (CDCS-DOP)

Pytest Configuration

Provides shared fixtures for all automated tests.

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
"""

import pytest

from app import create_app
from app.extensions import db


@pytest.fixture(scope="session")
def app():
    """
    Create a Flask application configured
    specifically for automated testing.
    """

    app = create_app()

    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        WTF_CSRF_ENABLED=False,
        LOGIN_DISABLED=False,
    )

    with app.app_context():

        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """
    Flask test client.
    """

    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    Flask CLI runner.
    """

    return app.test_cli_runner()


@pytest.fixture()
def app_context(app):
    """
    Application context for database operations.
    """

    with app.app_context():
        yield


@pytest.fixture()
def clean_database(app):
    """
    Ensure every test starts with a clean database.
    """

    with app.app_context():

        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())

        db.session.commit()

        yield

        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())

        db.session.commit()


@pytest.fixture(autouse=True)
def cleanup_login_session(client):
    """
    Ensure every test starts without an authenticated session.

    Prevents authentication state leakage
    between tests.
    """

    with client.session_transaction() as session:
        session.clear()

    yield

    with client.session_transaction() as session:
        session.clear()



