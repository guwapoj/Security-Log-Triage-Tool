
import pandas as pd
 
def load_logs(file_path):
    """
    Load Windows Security Event logs exported as CSV.
 
    Windows Event Viewer exports produce a CSV with 6 data columns
    but only 5 named headers, causing pandas to shift all values left
    by one column. This function handles that misalignment by
    explicitly supplying all 6 column names and skipping the original header row.
    """
    logs = pd.read_csv(
        file_path,
        encoding="utf-8-sig",  # strips the BOM (byte order mark) Windows adds
        names=["Keywords", "Date and Time", "Source", "Event ID", "Task Category", "Description"],
        skiprows=1
    )
    return logs
 