import pandas as pd

# Load login data
df = pd.read_csv("security_logs.csv")

# Keep only failed logins
failed_df = df[df["status"] == "FAILED"]

# Group by username
user_summary = failed_df.groupby("username").agg({
    "attempts": "sum"
}).reset_index()

# Risk scoring logic
def calculate_risk(attempts):
    if attempts >= 20:
        return "CRITICAL"
    elif attempts >= 10:
        return "HIGH"
    elif attempts >= 5:
        return "MEDIUM"
    else:
        return "LOW"

# Apply risk scores
user_summary["risk_level"] = user_summary["attempts"].apply(calculate_risk)

# Sort highest risk first
user_summary = user_summary.sort_values(by="attempts", ascending=False)

print("=== USER RISK SCORES ===")
print(user_summary)
