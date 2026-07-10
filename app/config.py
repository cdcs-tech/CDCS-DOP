"""
CDCS Digital Operations Platform (CDCS-DOP)

Application Configuration

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.5.5 – Session Security Review
"""

import os
from datetime import timedelta

from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    Base application configuration.
    """

    # ----------------------------------------------------
    # Security
    # ----------------------------------------------------

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    # Session Security

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"

    SESSION_COOKIE_SECURE = False

    PERMANENT_SESSION_LIFETIME = timedelta(
        hours=8
    )

    # Flask-Login Remember Me Security

    REMEMBER_COOKIE_HTTPONLY = True

    REMEMBER_COOKIE_SAMESITE = "Lax"

    REMEMBER_COOKIE_SECURE = False

    REMEMBER_COOKIE_DURATION = timedelta(
        days=14
    )


    # ----------------------------------------------------
    # Database Configuration
    # ----------------------------------------------------

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///"
        + os.path.join(
            BASE_DIR,
            "..",
            "instance",
            "cdcs.db"
        )
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
    """
    Development environment.
    """

    DEBUG = True

    ENV_NAME = "Development"



class TestingConfig(Config):
    """
    Testing environment.
    """

    TESTING = True

    ENV_NAME = "Testing"

    SESSION_COOKIE_SECURE = False

    REMEMBER_COOKIE_SECURE = False



class ProductionConfig(Config):
    """
    Production environment.

    HTTPS is mandatory.
    """

    DEBUG = False

    ENV_NAME = "Production"

    SESSION_COOKIE_SECURE = True

    REMEMBER_COOKIE_SECURE = True



config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}