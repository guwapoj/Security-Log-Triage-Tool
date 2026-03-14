import argparse

from parser import load_logs
from detections import (
    detect_failed_logins,
    detect_account_lockouts,
    detect_bruteforce,
    detect_success_after_failures,
    detect_privileged_logins
)

from report_generator import generate_report


# CLI argument parser
parser = argparse.ArgumentParser(description="Security Log Triage Tool")

parser.add_argument(
    "--file",
    required=True,
    help="Path to the security log CSV file"
)

args = parser.parse_args()

print("Loading logs...")

logs = load_logs(args.file)

print("Running security analysis...")

failed = detect_failed_logins(logs)
lockouts = detect_account_lockouts(logs)
bruteforce = detect_bruteforce(logs)
compromise = detect_success_after_failures(logs)
privileged = detect_privileged_logins(logs)

print("\n=== Security Log Analysis Report ===")

print("Failed Login Attempts:", len(failed))
print("Account Lockouts:", len(lockouts))
print("Privileged Logins:", len(privileged))

if bruteforce:
    print("ALERT:", bruteforce)

if compromise:
    print("ALERT:", compromise)

report = generate_report(failed, lockouts, privileged, bruteforce, compromise)

print("\nReport generated:", report)