from config.settings import MODELS
from agent_core.model_wrappers import query_model
from memory.memory_handler import get_best_model
from utils.logger import logger

def route_task(task_description):
    remembered_model = get_best_model(task_description)
    models_to_try = [remembered_model] + [m for m in MODELS if m != remembered_model] if remembered_model else MODELS

    for model_name in models_to_try:
        logger.info(f"🔁 Trying model: {model_name}")
        response = query_model(model_name, task_description)
        if response:
            return response, model_name
    return "⚠️ No model could handle this task.", "None"
