import subprocess
import sys
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

LOG_FILE = os.path.join(BASE_DIR, "logs", "auth.log")
MODEL_FILE = os.path.join(BASE_DIR, "models", "hybrid_model.pkl")


def run_module(module):
    return subprocess.Popen([PYTHON, "-m", module], cwd=BASE_DIR)


def wait_for_logs(min_lines=20):
    print("⏳ Waiting for log generation...")

    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE) as f:
                lines = f.readlines()

            if len(lines) >= min_lines:
                print(f"✅ {len(lines)} log entries detected")
                return

        time.sleep(2)


if __name__ == "__main__":

    print("\n🚀 BEHAVIOR-BASED IDS ATTACK TEST")
    print("====================================\n")

    # start GUI
    print("🔐 Launching Login System...")
    gui = run_module("app.login_gui")

    time.sleep(2)

    # start attack test
    print("💣 Launching Attack Test...")
    attacker = run_module("attacker.attack_test")

    # wait for logs
    wait_for_logs()

    # train model
    print("\n🧠 Training Hybrid Model...")
    subprocess.run([PYTHON, "-m", "ids.train_model"], cwd=BASE_DIR)

    if not os.path.exists(MODEL_FILE):
        print("❌ Model training failed")
        sys.exit()

    # start IDS
    print("\n🛡 Starting Real-Time IDS...\n")
    ids = run_module("ids.detect")

    print("\n✅ System Running — Watching for Attacks...\n")

    try:
        gui.wait()

    except KeyboardInterrupt:
        pass

    print("\n🛑 Stopping System...")

    attacker.terminate()
    ids.terminate()
    gui.terminate()

    print("System stopped cleanly.")