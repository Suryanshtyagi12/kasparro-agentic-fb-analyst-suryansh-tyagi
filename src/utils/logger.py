import json
import os
import datetime
import traceback

LOG_PATH = "logs/run_logs.json"

def _ensure_log_dir():
    os.makedirs("logs", exist_ok=True)

def log_event(event, details=None, level="INFO"):
    """
    Structured, JSON-based logging for all agents.
    Stores timestamp, event type, details, and log level.
    """
    _ensure_log_dir()

    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "level": level,
        "event": event,
        "details": details
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

def log_error(event, error: Exception):
    """
    Error logger with full stack trace for debugging.
    """
    _ensure_log_dir()

    error_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "level": "ERROR",
        "event": event,
        "error_message": str(error),
        "traceback": traceback.format_exc()
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(error_entry) + "\n")
