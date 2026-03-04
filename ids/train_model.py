import joblib
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from ids.feature_engineering import extract_features

LOG_FILE = "logs/auth.log"

features = extract_features(LOG_FILE)

X = features[[
    "total_attempts",
    "failed_attempts",
    "failed_ratio",
    "rate_change"
]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(
    n_estimators=400,
    contamination=0.1,
    random_state=42
)

model.fit(X_scaled)

joblib.dump((model, scaler), "models/hybrid_model.pkl")

print("✅ Hybrid ML model trained.")