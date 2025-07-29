import logging

# Configure logger
logger = logging.getLogger("RadhaRaniAgent")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formatter)

# Add handler if not already added (prevents duplicate logs)
if not logger.handlers:
    logger.addHandler(console_handler)
