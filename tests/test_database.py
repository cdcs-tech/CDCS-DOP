from app.extensions import db


def test_database_initialization(app):
    with app.app_context():
        assert db.engine is not None