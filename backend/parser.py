import re
from datetime import datetime
from typing import Dict, Any, Tuple, Optional

# Standard Log Pattern: YYYY-MM-DD HH:MM:SS [LEVEL] ServiceName: Message
LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+"
    r"\[(?P<level>[A-Z]+)\]\s+"
    r"(?P<service>[\w\.-]+):\s+"
    r"(?P<message>.*)$"
)

# Helper regex to pull IP addresses into metadata
IP_PATTERN = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

def parse_raw_log(raw_log: str) -> Tuple[Optional[datetime], str, str, str, Dict[str, Any]]:
    match = LOG_PATTERN.match(raw_log.strip())
    
    if not match:
        # Fallback for unstructured or unparseable logs
        return None, "UNKNOWN", "General", raw_log, {}

    data = match.groupdict()
    
    # Parse timestamp string to datetime object
    dt_obj = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
    
    # Extract metadata (e.g., IP addresses)
    metadata = {}
    ip_match = IP_PATTERN.search(data["message"])
    if ip_match:
        metadata["target_ip"] = ip_match.group(0)

    return dt_obj, data["level"], data["service"], data["message"], metadata