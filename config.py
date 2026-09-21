import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://eth-mainnet.public.blastapi.io",
    "retry_attempts": 3,
    "timeout": 30,
    "debug": False
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallbacks."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Configuration loading error: {e}. Using defaults.")

    return config

if __name__ == "__main__":
    # Example usage for crypto automation tool
    app_config = load_config()
    print(f"Active RPC: {app_config['rpc_url']}")