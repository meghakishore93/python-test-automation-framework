import requests
from utils.config_reader import read_config

config = read_config()

class UserAPI:
    def __init__(self):
        self.base_url = config["base_url"]
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def get_users(self, page=1):
        return requests.get(f"{self.base_url}/users", params={"page": page}, headers=self.headers)

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return requests.post(f"{self.base_url}/users", json=payload, headers=self.headers)
