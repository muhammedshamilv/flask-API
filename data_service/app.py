from flask import Flask,jsonify

from settings import secret_key
app = Flask(__name__)


app.config['SECRET_KEY'] = secret_key


def health_check():
    return jsonify({"health": "OK"}), 200

from data_service_app.urls import connection, auth

app.register_blueprint(connection)
app.register_blueprint(auth)
