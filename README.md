AuthLog Analyzer

Overview

AuthLog Analyzer is a Python-based security automation tool that analyzes Linux authentication logs and identifies suspicious SSH login activity.

The tool parses authentication events, extracts usernames and source IP addresses using regular expressions, aggregates failed login attempts, tracks targeted accounts, and assigns severity levels to support analyst triage and investigation.

Features

* Parses Linux authentication logs
* Detects failed SSH login attempts
* Extracts usernames and source IP addresses using regex
* Aggregates failed attempts by IP address
* Tracks targeted user accounts
* Assigns severity levels based on failed attempt counts
* Generates analyst-friendly reports

Technologies Used

* Python
* Regular Expressions (Regex)
* Linux Authentication Logs
* Dictionaries (Hash Maps)
* Security Automation

Detection Logic

The tool searches for failed SSH authentication attempts and extracts:

* Username
* Source IP Address

Failed attempts are aggregated by source IP.

Severity levels are assigned using the following thresholds:

Failed Attempts	Severity
1–3	LOW
4–5	MEDIUM
6+	HIGH

Sample Output

=========================
Suspicious IP Report
=========================
IP Address: 192.0.2.10
Failed Attempts: 5
Users Targeted:
- testuser
Severity: MEDIUM

Example Log Entry

May 27 23:29:25 localhost sshd[1850]: Failed password for testuser from 192.0.2.10 port 57748 ssh2

Skills Demonstrated

* Security Automation
* Log Analysis
* Detection Engineering
* Python Scripting
* Regex Field Extraction
* Incident Triage Concepts
* Linux Security Monitoring

Future Improvements

* Export reports to text files
* Add timestamp correlation
* Detect credential spraying activity
* Generate CSV reports
* Add geolocation enrichment
* Integrate with SIEM workflows

