from flask import Flask, request,jsonify
from processing_service_app.utils import generate_unique_api_key,decode_token,decode_api_key
import requests
logging_service_url = "http://logging_service:8001"  

app = Flask(__name__)

def generate_api_key():
    
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authorization header missing"}), 400

    token = token.replace("Bearer ", "")

    user_id=decode_token(token)

    if not user_id:
        return jsonify({"error": "Invalid token"}), 401

    api_key = generate_unique_api_key(user_id)
    log_payload = {"user_id":user_id,"username": "null", "activity_type": "api_key_generation"}
    response = requests.post(f"{logging_service_url}/log_activity",json=log_payload)

    return jsonify({"api_key": api_key}), 200


