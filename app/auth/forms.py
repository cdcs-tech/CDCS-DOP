"""
CDCS Digital Operations Platform (CDCS-DOP)

Authentication Forms

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.4 – Login Interface & Authentication Flow
"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    User login form.

    Authentication is performed using email
    and password credentials.
    """

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Length(max=120)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    remember = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Login"
    )