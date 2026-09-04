import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "max_retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "dry_run": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with default values.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Basic validation for essential crypto configuration keys.
    """
    required_keys = ["rpc_url", "max_retries"]
    return all(key in config for key in required_keys)

if __name__ == "__main__":
    # Example usage for automation-tool-45
    current_config = load_config()
    if validate_config(current_config):
        print(f"Loaded config with RPC: {current_config['rpc_url']}")