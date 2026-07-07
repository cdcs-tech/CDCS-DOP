from flask import Blueprint, render_template
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def home():
    dashboard_data = {
        "version": "1.0.0-alpha",
        "organization": "Career Development & Consultancy Services (CDCS)",
        "current_date": datetime.now().strftime("%d %B %Y"),
        "environment": "Development",
        "database_status": "Connected",
        "platform_status": "Operational"
    }

    return render_template(
        "dashboard/index.html",
        dashboard=dashboard_data
    )


@dashboard_bp.route("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0.0-alpha"
    }