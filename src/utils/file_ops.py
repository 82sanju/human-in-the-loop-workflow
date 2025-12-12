import json
from pathlib import Path
import uuid

BASE = Path("human_feedback")

def save_pending(data):
    task_id = str(uuid.uuid4())
    filepath = BASE / "pending" / f"{task_id}.json"
    filepath.write_text(json.dumps(data, indent=4))
    return task_id, filepath

def load_if_exists(folder, task_id):
    path = BASE / folder / f"{task_id}.json"
    return json.loads(path.read_text()) if path.exists() else None

def move_to(folder, task_id, data):
    path = BASE / folder / f"{task_id}.json"
    path.write_text(json.dumps(data, indent=4))
