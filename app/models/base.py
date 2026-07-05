from datetime import datetime

from app.extensions import db


class BaseModel(db.Model):
    """
    Abstract base model providing common fields
    for all database tables.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )