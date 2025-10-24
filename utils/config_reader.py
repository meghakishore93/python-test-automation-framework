import yaml
import os

def read_config():
    config_path = os.path.join(os.getcwd(), "config", "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
