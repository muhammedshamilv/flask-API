import datetime
import jwt 
from app import app


def generate_token(user_id):
    print(user_id)
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.api_jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token
