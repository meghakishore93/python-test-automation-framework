import pytest
from api.user_api import UserAPI
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture(scope="module")
def user_api():
    return UserAPI()

def test_get_users(user_api):
    logger.info("Fetching list of users")
    response = user_api.get_users()
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user(user_api):
    logger.info("Creating a new user")
    response = user_api.create_user("Megha", "QA Engineer")
    json_data = response.json()
    assert response.status_code == 201
    assert json_data["name"] == "Megha"
