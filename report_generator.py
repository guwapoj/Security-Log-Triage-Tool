

import os
from datetime import datetime
 
def generate_report(failed, lockouts, privileged, bruteforce, compromise):
    os.makedirs("reports", exist_ok=True)
    report_file = "reports/security_report.html"
 
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("""<html>
<head>
  <title>Security Log Analysis Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
    h1 { color: #222; }
    h2 { color: #444; border-bottom: 1px solid #ccc; padding-bottom: 4px; }
    .summary-box { background: white; padding: 20px; border-radius: 6px; margin-bottom: 20px; }
    .alert { background: #ffe0e0; border-left: 4px solid #cc0000; padding: 10px 16px; margin: 8px 0; border-radius: 4px; }
    .ok { color: #2a7a2a; font-weight: bold; }
    table { border-collapse: collapse; width: 100%; background: white; }
    th { background: #333; color: white; padding: 8px 12px; text-align: left; }
    td { padding: 7px 12px; border-bottom: 1px solid #ddd; font-size: 0.9em; }
    tr:hover { background: #f9f9f9; }
  </style>
</head>
<body>
""")
        f.write("<h1>Security Log Analysis Report</h1>")
        f.write(f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>")
 
        f.write("<div class='summary-box'><h2>Summary</h2>")
        f.write(f"<p>Failed Login Attempts: <b>{len(failed)}</b></p>")
        f.write(f"<p>Account Lockouts: <b>{len(lockouts)}</b></p>")
        f.write(f"<p>Privileged Logins: <b>{len(privileged)}</b></p>")
        f.write("</div>")
 
        f.write("<h2>Alerts</h2>")
        if bruteforce:
            f.write(f"<div class='alert'><b>⚠ ALERT:</b> {bruteforce}</div>")
        if compromise:
            f.write(f"<div class='alert'><b>⚠ ALERT:</b> {compromise}</div>")
        if not bruteforce and not compromise:
            f.write("<p class='ok'>✔ No critical alerts detected.</p>")
 
        # Failed logins table
        if len(failed) > 0:
            f.write("<h2>Failed Login Events</h2>")
            f.write("<table><tr><th>Date and Time</th><th>Event ID</th><th>Task Category</th></tr>")
            for _, row in failed.iterrows():
                f.write(f"<tr><td>{row['Date and Time']}</td><td>{row['Event ID']}</td><td>{row['Task Category']}</td></tr>")
            f.write("</table>")
 
        # Lockouts table
        if len(lockouts) > 0:
            f.write("<h2>Account Lockout Events</h2>")
            f.write("<table><tr><th>Date and Time</th><th>Event ID</th><th>Task Category</th></tr>")
            for _, row in lockouts.iterrows():
                f.write(f"<tr><td>{row['Date and Time']}</td><td>{row['Event ID']}</td><td>{row['Task Category']}</td></tr>")
            f.write("</table>")
 
        f.write("</body></html>")
 
    return report_file