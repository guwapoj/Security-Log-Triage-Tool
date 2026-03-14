

def detect_failed_logins(logs):
    """Detect all failed login attempts (Event ID 4625)."""
    failed = logs[logs["Keywords"] == "Audit Failure"]
    return failed
 
 
def detect_account_lockouts(logs):
    """Detect account lockout events (Event ID 4740)."""
    lockouts = logs[logs["Event ID"] == 4740]
    return lockouts
 
 
def detect_privileged_logins(logs):
    """Detect privileged account logins (Event ID 4672 - Special Logon)."""
    # Event ID 4672 is the numeric ID for Special Logon / privilege assignment
    privileged = logs[logs["Event ID"] == 4672]
    return privileged
 
 
def detect_bruteforce(logs):
    """Flag possible brute-force if 5 or more failed login attempts exist."""
    failed = logs[logs["Keywords"] == "Audit Failure"]
    if len(failed) >= 5:
        return f"Possible brute force activity detected ({len(failed)} failed attempts)"
    return None
 
 
def detect_success_after_failures(logs):
    """
    Detect potential account compromise: a successful login (4624) occurred
    in the same session as one or more prior failed attempts (4625).
    This pattern may indicate a successful brute-force or credential attack.
    """
    failed = logs[logs["Keywords"] == "Audit Failure"]
    success = logs[logs["Event ID"] == 4624]
 
    if len(failed) > 0 and len(success) > 0:
        return (
            f"Successful login(s) detected after {len(failed)} failure(s) — "
            "possible account compromise"
        )
    return None