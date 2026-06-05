import pandas as pd

# Load dataset
df = pd.read_csv("security_logs.csv")

# Group login attempts by user
user_attempts = df.groupby("username")["attempts"].sum()

# Calculate average attempts
average_attempts = user_attempts.mean()

print("=== LOGIN SPIKE DETECTION ===")
print(f"Average login attempts: {average_attempts}\n")

# Detect spikes
for user, attempts in user_attempts.items():
    if attempts > average_attempts * 2:
        print(f"ANOMALY DETECTED: {user} has unusually high activity ({attempts} attempts)")
