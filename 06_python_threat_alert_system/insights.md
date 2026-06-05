# Automated Threat Detection Insights

## Project Summary
This project simulates a Python-based security monitoring system designed to detect suspicious authentication behavior and generate automated alerts.

The system analyzes login activity data to identify:
- repeated failed login attempts
- suspicious IP addresses
- high-risk authentication patterns
- possible brute-force behavior

## Key Findings

### High-Risk User Activity
Multiple failed login attempts were detected for privileged accounts such as:
- admin
- root

Repeated failures against these accounts may indicate targeted access attempts.

### Suspicious IP Detection
The system identified recurring high-risk IP addresses associated with elevated failed login activity.

These IPs generated repeated authentication failures and triggered automated alerts.

### Automated Threat Monitoring
The alert system automatically:
- reads login log data
- identifies suspicious behavior
- classifies risky activity
- generates security alert reports

## Conclusion
This project demonstrates how Python can be used to automate security monitoring workflows and support SOC-style threat detection processes.
