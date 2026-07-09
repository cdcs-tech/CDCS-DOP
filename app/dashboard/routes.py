from datetime import datetime

from flask import render_template
from flask_login import login_required

from . import dashboard_bp


@dashboard_bp.route("/", endpoint="home")
@login_required
def home():
    """
    Enterprise Dashboard Home Page.

    This route serves as the primary landing page for
    authenticated users after a successful login.
    """

    dashboard = {
        "organization": "Career Development & Consultancy Services (CDCS)",
        "version": "1.0.0-alpha",
        "current_date": datetime.now().strftime("%d %B %Y"),
        "database_status": "Connected",
        "environment": "Development",
        "platform_status": "Healthy",
    }

    return render_template(
        "dashboard/index.html",
        dashboard=dashboard
    )