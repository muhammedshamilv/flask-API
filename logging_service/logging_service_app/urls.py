
from flask import Blueprint
from app import health_check
from logging_service_app.controllers.logs import log_activity
from app import get_logs
connection = Blueprint("connection", __name__, url_prefix="/")
logs = Blueprint("logs", __name__, url_prefix="/")

connection.add_url_rule("", view_func=health_check, methods=["GET"])

logs.add_url_rule("/log_activity", view_func=log_activity, methods=["POST"])

logs.add_url_rule(
    "/logs", view_func=get_logs, methods=["GET"]
)
