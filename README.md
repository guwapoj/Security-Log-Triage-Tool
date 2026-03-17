<div align="center">

#  Security Log Triage Tool

**Hands-on SOC analysis using your own Windows Security logs — no SIEM required.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-latest-150458?style=flat&logo=pandas&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)
![Purpose](https://img.shields.io/badge/Purpose-Educational-green?style=flat)

<!-- SCREENSHOT: Add a screenshot of the HTML report here once generated -->
<!-- To add: save your screenshot to /screenshots/report_preview.png and uncomment the line below -->
<!-- ![Report Preview](screenshots/report_preview.png) -->

</div>

---

##  Overview

Learning SOC analysis is hard when you have no logs to practice with. This tool fixes that.

Export your own Windows Security Event logs from Event Viewer, run a single command, and get a full HTML report flagging suspicious activity — failed logins, brute force attempts, account lockouts, and more. The same event types real SOC analysts monitor every day, analyzed on your own machine.

---

##  Features

-  Detects **failed login attempts** (Event ID 4625)
-  Flags **possible brute force** activity (5+ failures)
-  Identifies **successful logins after failures** — possible account compromise
-  Detects **account lockouts** (Event ID 4740)
-  Tracks **privileged account logins** (Event ID 4672)
-  Generates a clean **HTML incident report**

---

##  Detection Rules

| Event ID | Event Type | Detection |
|:---:|---|---|
| `4625` | Failed Login | Flagged individually + brute force threshold |
| `4624` | Successful Login | Cross-referenced against prior failures |
| `4740` | Account Lockout | Flagged directly |
| `4672` | Special Logon | Privileged access tracking |

---

##  Getting Started

### 1. Export your Windows Security Logs

1. Press `Win + R` → type `eventvwr` → press Enter
2. Go to **Windows Logs → Security**
3. Right panel → click **Save All Events As...**
4. Choose format: **CSV (Comma Separated)**
5. Save to the `sample_logs/` folder

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the tool

```bash
python triage.py --file sample_logs/security_logs.csv
```

### 4. View the report

Open `reports/security_report.html` in your browser.

---

##  Example Output

<!-- SCREENSHOT: Add a screenshot of your terminal output here -->
<!-- Save to /screenshots/terminal_output.png and uncomment the line below -->
<!-- ![Terminal Output](screenshots/terminal_output.png) -->

```
Loading logs...
Running security analysis...

=== Security Log Analysis Report ===
Failed Login Attempts: 37
Account Lockouts: 2
Privileged Logins: 917
ALERT: Possible brute force activity detected (37 failed attempts)
ALERT: Successful login(s) detected after 37 failure(s) — possible account compromise

Report generated: reports/security_report.html
```

<!-- SCREENSHOT: Add a screenshot of the full HTML report output here -->
<!-- Save to /screenshots/html_report.png and uncomment the line below -->
<!-- ![HTML Report](screenshots/html_report.png) -->

---

##  Project Structure

```
security-log-triage/
│
├── triage.py               # CLI entry point
├── parser.py               # CSV log loader
├── detections.py           # Detection logic
├── report_generator.py     # HTML report builder
├── requirements.txt
│
├── sample_logs/            # Drop your exported CSV here
│   └── .gitkeep
└── reports/                # Generated reports saved here
    └── .gitkeep
```

---

##  Requirements

- Python 3.8+
- pandas

```bash
pip install pandas
```

---

##  Who This Is For

| Audience | How it helps |
|---|---|
|  Cybersecurity students | Hands-on log analysis without an enterprise lab |
|  Aspiring SOC analysts | Practice real detection workflows |
|  Detection engineering learners | Understand how detection rules are built |
|  Curious Windows users | See what's actually happening on your machine |

---

##  Future Improvements

- [ ] Off-hours login detection
- [ ] IP-based attack correlation
- [ ] Native `.evtx` log format support
- [ ] Additional MITRE ATT&CK-aligned detection rules
- [ ] SIEM export compatibility

---

##  Disclaimer

This tool is intended for **educational purposes only**. Only analyze logs on systems you own or have explicit permission to inspect.

---

<div align="center">

Made for SOC learners, by a SOC learner.

</div>
