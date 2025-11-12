import json
import os

def save_feedback(data: dict, path="data/feedback.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)
    with open(path, "r+") as f:
        records = json.load(f)
        records.append(data)
        f.seek(0)
        json.dump(records, f, indent=2)
