import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "cdcs-development-key")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///cdcs.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False