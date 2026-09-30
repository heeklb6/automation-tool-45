import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "max_retries": 3,
    "timeout": 30,
    "dry_run": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config file: {e}. Using defaults.")
            
    return config

def get_env_overrides(config: Dict[str, Any]) -> Dict[str, Any]:
    """Overrides config values with environment variables."""
    for key in config:
        env_val = os.getenv(f"AUTO_{key.upper()}")
        if env_val is not None:
            # Handle type casting for environment variables
            if isinstance(config[key], bool):
                config[key] = env_val.lower() in ("true", "1", "yes")
            elif isinstance(config[key], int):
                config[key] = int(env_val)
            else:
                config[key] = env_val
    return config