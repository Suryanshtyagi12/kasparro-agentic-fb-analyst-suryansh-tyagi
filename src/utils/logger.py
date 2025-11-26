import json

def log_event(event_type, data):
    def make_json_safe(obj):
        if isinstance(obj, dict):
            return {str(k): make_json_safe(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [make_json_safe(i) for i in obj]
        else:
            return str(obj)

    safe_data = make_json_safe(data)

    with open("logs/run_logs.json", "a") as f:
        f.write(json.dumps({"event": event_type, "data": safe_data}) + "\n")
