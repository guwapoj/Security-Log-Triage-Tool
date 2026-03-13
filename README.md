A beginner-friendly Python tool that helps you get hands-on experience with SOC (Security Operations Center) analysis — using your own Windows Security logs.
Export your logs from Event Viewer, run one command, and instantly see suspicious activity flagged and summarized in an HTML report. No SIEM, no enterprise lab required.

Why This Exists
One of the hardest parts of learning SOC analysis is finding real logs to practice with. This tool solves that by letting you analyze your own machine's Windows Security Event logs — the same event types that real SOC analysts monitor every day.

What It Detects
DetectionEvent IDDescriptionFailed login attempts4625Repeated authentication failuresBrute force activity46255+ failed attempts flagged as possible attackAccount compromise4624 + 4625Successful login after multiple failuresAccount lockouts4740Accounts locked due to failed attemptsPrivileged logins4672Special privileges assigned to a session

How to Export Your Windows Logs

Press Win + R, type eventvwr, hit Enter
Navigate to Windows Logs → Security
In the right panel, click Save All Events As...
Save as CSV (Comma Separated) format
Place the file in the sample_logs/ folder


Installation
bashgit clone https://github.com/yourusername/security-log-triage.git
cd security-log-triage
pip install -r requirements.txt

Usage
bashpython triage.py --file sample_logs/security_logs.csv
Example Output
Loading logs...
Running security analysis...

=== Security Log Analysis Report ===
Failed Login Attempts: 37
Account Lockouts: 2
Privileged Logins: 917
ALERT: Possible brute force activity detected (37 failed attempts)
ALERT: Successful login(s) detected after 37 failure(s) — possible account compromise

Report generated: reports/security_report.html
Open reports/security_report.html in your browser for the full report.

Project Structure
security-log-triage/
├── triage.py            # Main entry point (CLI)
├── parser.py            # CSV log loader
├── detections.py        # Detection logic
├── report_generator.py  # HTML report builder
├── requirements.txt
├── sample_logs/         # Place your exported CSV here
└── reports/             # Generated reports output here

Requirements

Python 3.8+
pandas


Who This Is For

Cybersecurity students wanting hands-on log analysis experience
Aspiring SOC analysts learning detection workflows
Anyone curious about what's happening on their own machine


Future Improvements

Off-hours login detection
IP-based attack correlation
EVTX (native Windows log format) support
Additional detection rules


Disclaimer
This tool is intended for educational purposes only. Only analyze logs from systems you own or have permission to inspect.
