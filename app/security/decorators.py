"""
CDCS Digital Operations Platform (CDCS-DOP)

Authorization Decorators

Milestone 2 – Authentication & Security
Package 2.2 – Authorization & RBAC
Stage 2.2.5 – Authorization Decorators & Route Protection
"""

from functools import wraps

from flask import abort

from app.services.authorization_service import AuthorizationService


def role_required(role_name):
    """
    Restrict access to users with the specified role.

    Authentication is expected to be handled by
    Flask-Login's @login_required decorator.
    """

    def decorator(view):

        @wraps(view)
        def wrapped(*args, **kwargs):

            from flask_login import current_user

            if not AuthorizationService.user_has_role(
                current_user,
                role_name
            ):
                abort(403)

            return view(*args, **kwargs)

        return wrapped

    return decorator


def permission_required(permission_name):
    """
    Restrict access to users with the specified permission.

    Authentication is expected to be handled by
    Flask-Login's @login_required decorator.
    """

    def decorator(view):

        @wraps(view)
        def wrapped(*args, **kwargs):

            from flask_login import current_user

            if not AuthorizationService.user_has_permission(
                current_user,
                permission_name
            ):
                abort(403)

            return view(*args, **kwargs)

        return wrapped

    return decorator