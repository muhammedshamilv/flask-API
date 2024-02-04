from flask import request,jsonify
import datetime
activity_log={

}

import uuid

def generate_unique_user_id():
    return str(uuid.uuid4())

def log_activity():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    activity_type = data.get('activity_type')
    time=datetime.datetime.now()
    uuid=generate_unique_user_id()
    activity_log[uuid] = {"username": username, "user_id":user_id, "activity_type": activity_type,"time":time}
    return jsonify({"message": "Activity logged successfully"}), 200


