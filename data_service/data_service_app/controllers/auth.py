from flask import request,jsonify
import requests
from data_service_app.utils import generate_token
storage_service_url = "http://storage:8003"  
logging_service_url = "http://logging_service:8001"

def register_user():
    data = request.get_json()    
    if "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data["username"]
    password = data["password"]
    response = requests.get(f"{storage_service_url}/get_all_users")
    if response.status_code == 200:
        all_users = response.json()
        if username in all_users:
            return jsonify({"error": "Username already exists"}), 400
        else:
            payload = {"username": username, "password": password}
            response = requests.post(f"{storage_service_url}/store_user",json=payload)
            if response.status_code == 201:
                data = response.json()
        
                log_payload = {"user_id":data["id"],"username": username, "activity_type": "registration"}
                response = requests.post(f"{logging_service_url}/log_activity",json=log_payload)
                return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "Failed to retrieve user data from storage service"}), 500


def login_user():
    data = request.get_json()

    if "username" not in data or "password" not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data["username"]
    password = data["password"]
    response = requests.get(f"{storage_service_url}/get_all_users")
    if response.status_code == 200:
        all_users = response.json()
        print(all_users)
        if username not in all_users or all_users[username]["password"] != password:
            return jsonify({"error": "Invalid username or password"}), 401
        else:

            log_payload = {"user_id": all_users[username]["user_id"],"username": username, "activity_type": "login"}
            response = requests.post(f"{logging_service_url}/log_activity",json=log_payload)
    
    user_id = str(all_users[username]["user_id"])
    token = generate_token(user_id)


    return jsonify({"token": token}), 200


