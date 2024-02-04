import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
logs_user_name = os.getenv("LOGS_USER_NAME")
logs_password = os.getenv("LOGS_PASSWORD")



