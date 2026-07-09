"""
CDCS Digital Operations Platform (CDCS-DOP)

Authentication Routes

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.4 – Login Interface & Authentication Flow
"""

from flask import (
    flash,
    redirect,
    render_template,
    url_for
)

from flask_login import login_user

from app.auth import auth_bp
from app.auth.forms import LoginForm
from app.models.user import User


@auth_bp.route("/")
def index():
    """
    Authentication module landing page.
    """

    return render_template("auth/index.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Authenticate users using email and password.
    """

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and user.check_password(
            form.password.data
        ):

            if not user.is_active:
                flash(
                    "Your account is inactive. Please contact an administrator.",
                    "warning"
                )

                return redirect(
                    url_for("auth.login")
                )

            login_user(
                user,
                remember=form.remember.data
            )

            flash(
                "Login successful.",
                "success"
            )

            return redirect(
                url_for("dashboard.home")
            )

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template(
        "auth/login.html",
        form=form
    )