"""
CDCS Digital Operations Platform (CDCS-DOP)

Authentication Forms

Milestone 2 – Authentication & Security
Stage 2.4.1 – Login Interface Foundation
"""

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
)


class LoginForm(FlaskForm):
    """
    User login form.
    """

    email = StringField(
        "Email Address",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120),
        ],
        render_kw={
            "placeholder": "Enter your email address",
            "autocomplete": "email",
        },
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8),
        ],
        render_kw={
            "placeholder": "Enter your password",
            "autocomplete": "current-password",
        },
    )

    remember = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Sign In"
    )