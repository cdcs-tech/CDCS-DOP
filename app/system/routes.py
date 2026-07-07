from datetime import datetime

from flask import current_app, jsonify, render_template

from app.extensions import db
from app.system import system_bp


@system_bp.route("/health")
def health():

    database_status = "Connected"

    try:
        db.session.execute(db.text("SELECT 1"))
    except Exception:
        database_status = "Disconnected"

    health_data = {
        "application": "CDCS Digital Operations Platform",
        "organization": "Career Development & Consultancy Services (CDCS)",
        "version": "1.0.0-alpha",
        "environment": current_app.config.get("ENV_NAME"),
        "database": database_status,
        "status": "Healthy" if database_status == "Connected" else "Warning",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify(health_data)


@system_bp.route("/system")
def system_information():

    database_status = "Connected"

    try:
        db.session.execute(db.text("SELECT 1"))
    except Exception:
        database_status = "Disconnected"

    return render_template(
        "system/health.html",
        system={
            "application": "CDCS Digital Operations Platform",
            "organization": "Career Development & Consultancy Services (CDCS)",
            "version": "1.0.0-alpha",
            "environment": current_app.config.get("ENV_NAME"),
            "database": database_status,
            "status": "Healthy" if database_status == "Connected" else "Warning",
            "server_time": datetime.now().strftime("%d %B %Y %H:%M:%S")
        }
    )