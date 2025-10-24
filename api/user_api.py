import requests
from utils.config_reader import read_config

config = read_config()

class UserAPI:
    def __init__(self):
        self.base_url = config["base_url"]

    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page})

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return requests.post(f"{self.base_url}/users", json=payload)
