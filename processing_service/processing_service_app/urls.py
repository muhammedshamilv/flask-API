from flask import Blueprint
from processing_service_app.controllers.api_key import generate_api_key
from app import health_check

connection = Blueprint("connection", __name__, url_prefix="/")
api_key = Blueprint("api_key", __name__, url_prefix="/")

connection.add_url_rule("", view_func=health_check, methods=["GET"])

api_key.add_url_rule("/generate_api_key", view_func=generate_api_key, methods=["POST"])
