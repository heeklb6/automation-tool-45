import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='config/default.json'):
        self.default_config_path = default_config_path
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        config = self.load_json(self.default_config_path)
        # Override with environment variables if they exist
        env_config = self.load_env_config()
        config.update(env_config)
        return config

    def load_json(self, path):
        # Load configuration from JSON file
        if not os.path.isfile(path):
            return {}
        with open(path, 'r') as json_file:
            return json.load(json_file)

    def load_env_config(self):
        # Load configuration from environment variables
        env_config = {}
        for key in os.environ:
            if key.startswith('CRYPTO_'):
                env_config[key[7:]] = os.environ[key]
        return env_config

    def get(self, key, default=None):
        # Retrieve a configuration value
        return self.config.get(key, default)

# Example usage of the ConfigLoader
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('API_KEY', 'default_api_key'))