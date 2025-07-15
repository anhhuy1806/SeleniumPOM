import json
import os

class ConfigReader:
    _config = None

    #Loads the configuration from a JSON file
    @staticmethod
    def read_json():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        return ConfigReader.read_json()['base_url']
    
    @staticmethod
    def get_username():
        return ConfigReader.read_json()['credentials']['username']
    
    @staticmethod
    def get_password():
        return ConfigReader.read_json()['credentials']['password']
    
    @staticmethod
    def get_login_api():
        return ConfigReader.read_json()["login_api"]
