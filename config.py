import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load_config(self, filepath):
        try:
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        except FileNotFoundError:
            print(f'Config file not found, using default settings.')
        except json.JSONDecodeError:
            print(f'Error decoding JSON, using default settings.')

    def get_config(self):
        return {**self.default_config, **self.user_config}

# Default configuration
DEFAULT_CONFIG = {
    'api_key': 'your_api_key_here',
    'timeout': 30,
    'retries': 3,
}

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader(DEFAULT_CONFIG)
    config_loader.load_config('config.json')
    config = config_loader.get_config()
    print(config)  # Display the final configuration settings