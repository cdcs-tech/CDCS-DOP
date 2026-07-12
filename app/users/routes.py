"""
CDCS Digital Operations Platform (CDCS-DOP)

User Management Routes

Milestone 2 – Authentication & Security
Package 2.3 – User Management
Stage 2.3.5 – User Management API & Route Integration
"""

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from flask_login import login_required

from app.users import users_bp
from app.security.decorators import permission_required
from app.services.user_service import UserService

from app.models.user import User
from app.models.role import Role


# ==========================================================
# User List
# ==========================================================

@users_bp.route("/")
@login_required
@permission_required("users.view")
def index():
    """
    Display all users.
    """

    users = User.query.order_by(
        User.full_name
    ).all()

    return render_template(
        "users/index.html",
        users=users,
    )


# ==========================================================
# User Details
# ==========================================================

@users_bp.route("/<int:user_id>")
@login_required
@permission_required("users.view")
def detail(user_id):
    """
    Display a user's profile.
    """

    user = User.query.get_or_404(user_id)

    return render_template(
        "users/detail.html",
        user=user,
    )


# ==========================================================
# Create User
# ==========================================================

@users_bp.route(
    "/create",
    methods=["GET", "POST"]
)
@login_required
@permission_required("users.create")
def create():
    """
    Create a new user.
    """

    if request.method == "POST":

        UserService.create_user(
            full_name=request.form["full_name"],
            email=request.form["email"],
            password=request.form["password"],
        )

        flash(
            "User created successfully.",
            "success"
        )

        return redirect(
            url_for("users.index")
        )

    return render_template(
        "users/create.html"
    )


# ==========================================================
# Edit User
# ==========================================================

@users_bp.route(
    "/<int:user_id>/edit",
    methods=["GET", "POST"]
)
@login_required
@permission_required("users.update")
def edit(user_id):
    """
    Update an existing user.
    """

    user = User.query.get_or_404(user_id)

    if request.method == "POST":

        UserService.update_user(
            user=user,
            full_name=request.form["full_name"],
            email=request.form["email"],
            is_active=(
                "is_active"
                in request.form
            ),
        )

        flash(
            "User updated successfully.",
            "success"
        )

        return redirect(
            url_for(
                "users.detail",
                user_id=user.id
            )
        )

    return render_template(
        "users/edit.html",
        user=user,
    )


# ==========================================================
# Activate User
# ==========================================================

@users_bp.route(
    "/<int:user_id>/activate",
    methods=["POST"]
)
@login_required
@permission_required("users.update")
def activate(user_id):
    """
    Activate a user account.
    """

    user = User.query.get_or_404(user_id)

    UserService.activate_user(user)

    flash(
        "User activated successfully.",
        "success"
    )

    return redirect(
        url_for(
            "users.detail",
            user_id=user.id
        )
    )


# ==========================================================
# Deactivate User
# ==========================================================

@users_bp.route(
    "/<int:user_id>/deactivate",
    methods=["POST"]
)
@login_required
@permission_required("users.update")
def deactivate(user_id):
    """
    Deactivate a user account.
    """

    user = User.query.get_or_404(user_id)

    UserService.deactivate_user(user)

    flash(
        "User deactivated successfully.",
        "success"
    )

    return redirect(
        url_for(
            "users.detail",
            user_id=user.id
        )
    )


# ==========================================================
# Assign Role
# ==========================================================

@users_bp.route(
    "/<int:user_id>/assign-role",
    methods=["POST"]
)
@login_required
@permission_required("users.assign_role")
def assign_role(user_id):
    """
    Assign a role to a user.
    """

    user = User.query.get_or_404(user_id)

    role = Role.query.get_or_404(
        request.form["role_id"]
    )

    UserService.assign_role(
        user=user,
        role=role,
    )

    flash(
        "Role assigned successfully.",
        "success"
    )

    return redirect(
        url_for(
            "users.detail",
            user_id=user.id
        )
    )