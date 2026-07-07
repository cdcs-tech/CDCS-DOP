from datetime import datetime

from flask import render_template

from . import dashboard_bp


@dashboard_bp.route("/", endpoint="home")
def home():
    """
    Enterprise Dashboard Home Page
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