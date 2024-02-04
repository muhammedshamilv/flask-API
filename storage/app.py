
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

import uuid

def generate_unique_user_id():
    return str(uuid.uuid4())

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"health": "OK"}), 200

@app.route('/store_user', methods=['POST'])
def store_user():
    data = request.get_json()
    if "username" not in data or "password" not in data :
        return jsonify({"error": "Incomplete data. Please provide username, password"}), 400

    username = data["username"]
    password = data["password"]
    user_id=generate_unique_user_id()

    users[username] = {"username": username, "password": password, "user_id": user_id}

    return jsonify({"message": f"User {username} stored successfully","id":user_id}), 201


@app.route('/get_all_users', methods=['GET'])
def get_all_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True, port=8003,host='0.0.0.0')