from app.extensions import db
from app.models.base import BaseModel


class User(BaseModel):
    """
    System users.
    """

    __tablename__ = "users"

    full_name = db.Column(db.String(120), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        default="Staff"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    def __repr__(self):
        return f"<User {self.email}>"