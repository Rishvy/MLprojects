import logging
import os
from datetime import datetime

# Correcting the LOG_FILE definition and string formatting
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Correcting the path definition and method call
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Correcting the log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Correcting the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

