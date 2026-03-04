import matplotlib.pyplot as plt
import joblib
import numpy as np
from ids.feature_engineering import extract_features

LOG_FILE = "logs/auth.log"

model, scaler = joblib.load("models/hybrid_model.pkl")

features = extract_features(LOG_FILE)

if features.empty:
    print("❌ No features available to visualize.")
    exit()

X = features[[
    "total_attempts",
    "failed_attempts",
    "failed_ratio",
    "rate_change"
]]

X_scaled = scaler.transform(X)

scores = model.decision_function(X_scaled)

plt.figure(figsize=(10, 5))
plt.plot(scores, label="Anomaly Score")
plt.axhline(y=0, color='r', linestyle='--', label="Decision Boundary")
plt.title("Hybrid Model Anomaly Score Over Time")
plt.xlabel("Time Window Index")
plt.ylabel("Anomaly Score")
plt.legend()
plt.tight_layout()
plt.show()