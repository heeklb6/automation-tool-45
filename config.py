import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://bsc-dataseed.binance.org/",
    "gas_limit": 21000,
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file, falling back to defaults
    for missing keys or missing files.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading config file: {e}. Using defaults.")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Basic schema validation for critical fields.
    """
    required_keys = ["rpc_url"]
    return all(key in config for key in required_keys)
