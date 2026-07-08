import logging
import os
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, render_template

from app.config import config
from app.extensions import db, migrate

from app.system import system_bp
from app.dashboard import dashboard_bp
from app.auth import auth_bp


def create_app(config_name="default"):
    app = Flask(__name__)

    # ----------------------------------------------------
    # Load Configuration
    # ----------------------------------------------------
    app.config.from_object(config[config_name])

    # ----------------------------------------------------
    # Initialize Extensions
    # ----------------------------------------------------
    db.init_app(app)
    migrate.init_app(app, db)

    # ----------------------------------------------------
    # Register Blueprints
    # ----------------------------------------------------
    app.register_blueprint(system_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    # ----------------------------------------------------
    # Error Handlers
    # ----------------------------------------------------
    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        db.session.rollback()
        return render_template("errors/500.html"), 500

    # ----------------------------------------------------
    # Logging Configuration
    # ----------------------------------------------------
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_handler = TimedRotatingFileHandler(
        "logs/cdcs_dop.log",
        when="midnight",
        interval=1,
        backupCount=30,
        encoding="utf-8"
    )

    log_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
    )

    log_handler.setFormatter(formatter)

    if log_handler not in app.logger.handlers:
        app.logger.addHandler(log_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info("CDCS-DOP application started successfully.")

    return app