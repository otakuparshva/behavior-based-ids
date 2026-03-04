import os
import time
import joblib
from ids.feature_engineering import extract_features

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE = os.path.join(BASE_DIR, "logs", "auth.log")
MODEL_FILE = os.path.join(BASE_DIR, "models", "hybrid_model.pkl")

print("🔄 Loading model...")

model, scaler = joblib.load(MODEL_FILE)

print("✅ Model loaded.")
print("\n🛡 Real-Time IDS Started...\n")

last_line_count = 0


def monitor():

    global last_line_count

    try:

        while True:

            with open(LOG_FILE, "r") as f:
                lines = f.readlines()

            current_line_count = len(lines)

            if current_line_count > last_line_count:

                print("📡 New log activity detected...")

                features = extract_features(LOG_FILE)

                if not features.empty:

                    X = features[[
                        "total_attempts",
                        "failed_attempts",
                        "failed_ratio",
                        "rate_change"
                    ]]

                    X_scaled = scaler.transform(X)

                    predictions = model.predict(X_scaled)

                    features["anomaly"] = predictions

                    anomalies = features[features["anomaly"] == -1]

                    if not anomalies.empty:

                        print("\n🚨🚨🚨 ATTACK DETECTED 🚨🚨🚨\n")

                        for _, row in anomalies.iterrows():

                            print(
                                f"IP: {row['ip']} | "
                                f"Attempts: {int(row['total_attempts'])} | "
                                f"Failed Ratio: {round(row['failed_ratio'],2)} | "
                                f"Rate Change: {round(row['rate_change'],2)}"
                            )

                        print("\n⚠ Suspicious login behaviour detected!\n")

                last_line_count = current_line_count

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 IDS stopped.")


if __name__ == "__main__":
    monitor()