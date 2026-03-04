import datetime
import random
import os
from app.database import validate_user

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "auth.log")

def generate_ip():
    return f"192.168.1.{random.randint(2, 254)}"

def login(username, password):
    ip = generate_ip()
    status = "SUCCESS" if validate_user(username, password) else "FAILED"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | user={username} | ip={ip} | status={status}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    return status