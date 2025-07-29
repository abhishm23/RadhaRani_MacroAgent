import json
from pathlib import Path

MEMORY_FILE = Path("memory") / "memory.json"
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
MEMORY_FILE.touch(exist_ok=True)

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_best_model(task):
    memory = load_memory()
    for keyword, record in memory.items():
        if keyword in task:
            return record["model"]
    return None

def remember_feedback(task, correction, model_name):
    memory = load_memory()
    memory[task[:50]] = {"model": model_name, "correction": correction}
    save_memory(memory)
