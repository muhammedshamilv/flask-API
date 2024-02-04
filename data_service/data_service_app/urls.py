from flask import Blueprint
from app import health_check
from data_service_app.controllers.auth import register_user,login_user
connection = Blueprint("connection", __name__, url_prefix="/")
auth = Blueprint("auth", __name__, url_prefix="/")

connection.add_url_rule("", view_func=health_check, methods=["GET"])

auth.add_url_rule("/register", view_func=register_user, methods=["POST"])

auth.add_url_rule(
    "login", view_func=login_user, methods=["POST"]
)
