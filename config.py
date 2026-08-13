import json
import os

DEFAULT_CONFIG = {
    'api_key': 'default_api_key',
    'api_secret': 'default_api_secret',
    'base_url': 'https://api.default.com',
    'timeout': 30
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()  # Start with default config
        self.load_config()  # Load config from file if it exists

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)  # Update with values from file

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=4)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader)  # Print the loaded configuration