import logging
import os

def get_logger(name="automation"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        log_dir = "reports"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, "test_log.log")

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
