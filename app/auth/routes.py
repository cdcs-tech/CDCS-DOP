"""
CDCS Digital Operations Platform (CDCS-DOP)
Authentication Routes

Milestone 2 – Authentication & Security
Package 2.1 – Authentication Foundation
Stage 2.1.1 – Authentication Blueprint Creation
"""

from flask import render_template

from app.auth import auth_bp


@auth_bp.route("/", methods=["GET"])
def index():
    """
    Authentication landing page.

    This placeholder page confirms that the Authentication
    Blueprint has been successfully registered.

    Future stages will replace this page with the Login view.
    """
    return render_template("auth/index.html")