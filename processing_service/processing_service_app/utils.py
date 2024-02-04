import jwt
from app import app
from cryptography.fernet import Fernet
import base64
import settings
app.config['SECRET_KEY'] = settings.secret_key
SECRET_KEY = settings.cipher
cipher_suite = Fernet(SECRET_KEY)


def generate_unique_api_key(user_id):
    user_id_bytes = str(user_id).encode('utf-8')
    encrypted_user_id = cipher_suite.encrypt(user_id_bytes)
    api_key = base64.urlsafe_b64encode(encrypted_user_id).decode('utf-8')
    return api_key

def decode_api_key(api_key):
    encrypted_user_id = base64.urlsafe_b64decode(api_key.encode('utf-8'))
    user_id_bytes = cipher_suite.decrypt(encrypted_user_id)
    user_id = user_id_bytes.decode('utf-8')
    return user_id


def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, str(app.config['SECRET_KEY']), algorithms=['HS256'])
        return decoded_payload.get('user_id')
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.InvalidTokenError:
        return None  