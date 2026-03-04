import time
import random
from app.auth_backend import login

TARGET_USER = "admin"

# intentionally WRONG passwords
ATTACK_PASSWORDS = [
    "admin1",
    "admin12",
    "admin111",
    "password123",
    "letmein123",
    "root123",
    "administrator",
    "adminpass",
    "passadmin",
    "123admin"
]

ATTEMPTS = 40


def simulate_attack():

    print("\n🚨 Starting Attack Simulation...\n")

    for i in range(ATTEMPTS):

        pwd = random.choice(ATTACK_PASSWORDS)

        result = login(TARGET_USER, pwd)

        print(f"Attempt {i+1} | password={pwd} | result={result}")

        # simulate burst attack
        time.sleep(0.1)

    print("\n⚠ Attack Simulation Finished\n")


if __name__ == "__main__":
    simulate_attack()