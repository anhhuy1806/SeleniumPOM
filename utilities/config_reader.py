import json
import os

class ConfigReader:
    @staticmethod
    def get_config():
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
        with open(path, "r") as file:
            return json.load(file)
