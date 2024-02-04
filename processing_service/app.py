from flask import Flask,jsonify


import settings
app = Flask(__name__)
secret_key= settings.secret_key
app.config['SECRET_KEY'] = secret_key

def health_check():
    return jsonify({"health": "OK"}), 200

from processing_service_app.urls import api_key, connection

app.register_blueprint(connection)
app.register_blueprint(api_key)
