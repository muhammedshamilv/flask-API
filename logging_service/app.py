from flask import Flask,jsonify
from flask_jwt_extended import JWTManager
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()
import settings
from logging_service_app.controllers.logs import activity_log
secret_key= settings.secret_key
app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

users = {
    settings.logs_user_name: {"password": settings.logs_password},
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username]["password"] == password:
        return username
    

@auth.login_required
def get_logs():
    logs = activity_log
    return jsonify(logs)
    
def health_check():
    return jsonify({"health": "OK"}), 200

from logging_service_app.urls import connection, logs

app.register_blueprint(connection)
app.register_blueprint(logs)
