import requests
import time

# Since GUI is local, we'll simulate login calls directly
from app.auth_backend import login

target_user = "admin"

password_list = [
    "123456",
    "password",
    "admin",
    "admin123",
    "letmein"
]

for pwd in password_list:
    result = login(target_user, pwd)
    print(f"Trying {pwd} -> {result}")
    time.sleep(0.5)