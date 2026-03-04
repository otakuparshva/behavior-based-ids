import pandas as pd
import numpy as np

def extract_features(log_file):
    df = pd.read_csv(log_file, sep="|", header=None)
    df.columns = ["timestamp", "user", "ip", "status"]

    df["timestamp"] = pd.to_datetime(df["timestamp"].str.strip())
    df["user"] = df["user"].str.strip().str.replace("user=", "")
    df["ip"] = df["ip"].str.strip().str.replace("ip=", "")
    df["status"] = df["status"].str.strip().str.replace("status=", "")

    df = df.sort_values("timestamp")

    # Convert success/failure to numeric
    df["failed"] = (df["status"] == "FAILED").astype(int)

    # 60-second rolling window per IP
    df.set_index("timestamp", inplace=True)

    features = []

    for ip, group in df.groupby("ip"):
        group = group.sort_index()

        rolling = group.rolling("60s")

        total_attempts = rolling["failed"].count()
        failed_attempts = rolling["failed"].sum()
        failed_ratio = failed_attempts / total_attempts

        rate_change = total_attempts.diff()

        temp_df = pd.DataFrame({
            "ip": ip,
            "total_attempts": total_attempts,
            "failed_attempts": failed_attempts,
            "failed_ratio": failed_ratio,
            "rate_change": rate_change
        })

        features.append(temp_df)

    feature_df = pd.concat(features).dropna()

    return feature_df.reset_index()