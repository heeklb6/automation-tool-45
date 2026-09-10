import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load {config_path}: {e}. Using defaults.")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Basic schema validation for essential crypto parameters.
    """
    required_keys = ["rpc_url", "timeout"]
    return all(key in config for key in required_keys)