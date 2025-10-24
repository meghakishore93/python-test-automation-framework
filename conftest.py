import pytest
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture(autouse=True)
def log_test_start_end():
    logger.info("===== Test Start =====")
    yield
    logger.info("===== Test End =====")
