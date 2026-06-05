import csv

failed_count = 0

with open("security_logs.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        username = row["username"]
        status = row["status"]
        ip = row["ip"]

        if status == "FAILED":

            failed_count += 1

            print("FAILED LOGIN:", username, ip)

            if username in ["admin", "root"]:
                print("CRITICAL ALERT")

            print()

print("Total failed logins:", failed_count)
