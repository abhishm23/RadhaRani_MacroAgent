import requests
from config.settings import OLLAMA_ENDPOINT
from utils.logger import logger

def query_model(model_name, prompt):
    try:
        response = requests.post(
            f"{OLLAMA_ENDPOINT}/api/generate",
            json={"model": model_name, "prompt": prompt, "stream": False}
        )
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        logger.error(f"❌ Model {model_name} failed with status {response.status_code}")
    except Exception as e:
        logger.exception(f"⚠️ Exception querying {model_name}: {e}")
    return None
