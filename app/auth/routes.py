"""
CDCS Digital Operations Platform (CDCS-DOP)

Authentication Routes

Milestone 2 – Authentication & Security
Stage 2.4.1 – Login Interface Foundation
"""

from app.auth import auth_bp
from urllib.parse import urlparse

from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.auth.forms import LoginForm
from app.models.user import User



# ----------------------------------------------------
# Login
# ----------------------------------------------------

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Authenticate a user.
    """

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data.strip().lower()
        ).first()

        if (
            user
            and user.is_active
            and user.check_password(form.password.data)
        ):

            login_user(
                user,
                remember=form.remember.data
            )

            flash(
                f"Welcome back, {user.full_name}.",
                "success",
            )

            next_page = request.args.get("next")

            if (
                next_page
                and urlparse(next_page).netloc == ""
            ):
                return redirect(next_page)

            return redirect(
                url_for("dashboard.home")
            )

        flash(
            "Invalid email or password.",
            "danger",
        )

    return render_template(
        "auth/login.html",
        title="Sign In",
        form=form,
    )


# ----------------------------------------------------
# Logout
# ----------------------------------------------------

@auth_bp.route("/logout")
@login_required
def logout():
    """
    Log out the current user.
    """

    logout_user()

    flash(
        "You have been logged out successfully.",
        "info",
    )

    return redirect(
        url_for("auth.login")
    )