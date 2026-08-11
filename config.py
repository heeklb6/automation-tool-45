import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()  

    def load_defaults(self):
        # Load default config from a JSON file
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Default config not found at {self.default_config_path}")
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def merge_with_environment(self):
        # Update config with environment variables if they exist
        for key in self.config:
            env_value = os.getenv(key)
            if env_value is not None:
                self.config[key] = env_value

    def get_config(self):
        # Return the final configuration
        self.merge_with_environment()
        return self.config

# Example usage:
# config_loader = ConfigLoader('default_config.json')
# config = config_loader.get_config()