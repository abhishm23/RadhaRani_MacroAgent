# router.py

import json
from models import mistral, codellama, gemma, phi

MODEL_ORDER = [mistral, codellama, gemma, phi]
MEMORY_PATH = "memory/memory.json"

def load_memory():
    try:
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(mem):
    with open(MEMORY_PATH, "w") as f:
        json.dump(mem, f, indent=4)

def route_task(task_type, prompt):
    memory = load_memory()
    if task_type in memory:
        model_name = memory[task_type]
        model = next((m for m in MODEL_ORDER if m.__name__.endswith(model_name)), None)
        if model:
            return model.generate(prompt)

    for model in MODEL_ORDER:
        try:
            output = model.generate(prompt)
            if "error" not in output.lower():  # placeholder scoring
                memory[task_type] = model.__name__.split('.')[-1]
                save_memory(memory)
                return output
        except Exception as e:
            print(f"{model.__name__} failed: {e}")
            continue

    return "All models failed. Try again or provide correction."