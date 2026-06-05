import pandas as pd

# Load dataset
df = pd.read_csv("security_logs.csv")

print("=== LOGIN DATA OVERVIEW ===")
print(df)

# Filter failed logins
failed_logins = df[df["status"] == "FAILED"]

print("\n=== FAILED LOGIN ACTIVITY ===")
print(failed_logins)

# Count failed attempts by user
user_summary = failed_logins.groupby("username").size()

print("\n=== FAILED LOGIN COUNT BY USER ===")
print(user_summary)

# Identify high-risk attempts
high_risk = df[df["attempts"] >= 10]

print("\n=== HIGH-RISK LOGIN EVENTS ===")
print(high_risk)
