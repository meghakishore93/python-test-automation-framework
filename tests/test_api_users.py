import pytest
from api.user_api import UserAPI
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture(scope="module")
def user_api():
    return UserAPI()

def test_get_users(user_api):
    logger.info("Fetching list of users")
    r = user_api.get_users()
    assert r.status_code in [200, 201]
    assert len(r.json()) > 0

def test_create_user(user_api):
    logger.info("Creating a new user")
    r = user_api.create_user("Megha", "QA Engineer")
    assert r.status_code in [200, 201]
