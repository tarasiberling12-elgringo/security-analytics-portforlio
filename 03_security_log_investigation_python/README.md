# security-log-investigation-system
Overview

This Python project analyzes security login logs from a CSV file and detects suspicious activity.

The script:

* detects failed logins
* identifies privileged account failures
* counts suspicious login attempts
* prints investigation alerts

⸻

Technologies Used

* Python
* CSV processing
* Dictionaries
* Loops and conditionals

⸻

Features

* Failed login detection
* Critical alert generation
* Structured CSV analysis
* Simple investigation workflow

____

Example Outputs

* FAILED LOGIN: admin 192.168.1.10
  CRITICAL ALERT
* FAILED LOGIN: root 192.168.1.12
  CRITICAL ALERT
* Total failed logins: 4
