"""
CDCS Digital Operations Platform (CDCS-DOP)

Pytest Configuration

Shared fixtures for all regression tests.
"""

import pytest

from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    """
    Create a fresh application for each test session.
    """

    app = create_app("testing")

    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
    )

    with app.app_context():

        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Flask test client.
    """

    return app.test_client()


@pytest.fixture(autouse=True)
def cleanup_auth_state():
    """
    Ensure authentication/session state is reset
    between tests.
    """

    yield