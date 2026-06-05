import csv

failed_attempts = {}
high_risk_ips = {}

with open("security_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        username = row["username"]
        ip = row["ip_address"]
        status = row["status"]
        attempts = int(row["attempts"])

        # Track failed attempts per user
        if status == "FAILED":
            failed_attempts[username] = failed_attempts.get(username, 0) + 1

        # Track high-risk IPs
        if attempts >= 10:
            high_risk_ips[ip] = high_risk_ips.get(ip, 0) + 1

print("=== SECURITY ALERT REPORT ===")

print("\nHigh-Risk Users:")
for user, count in failed_attempts.items():
    if count >= 2:
        print(f"ALERT: {user} has {count} failed login attempts")

print("\nSuspicious IP Addresses:")
for ip, count in high_risk_ips.items():
    print(f"WARNING: {ip} triggered {count} high-risk events")
