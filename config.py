import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://bsc-dataseed.binance.org/",
    "retry_attempts": 3,
    "gas_price_gwei": 5,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Config error: {e}, using defaults")
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Helper for accessing specific config values."""
    config = load_config()
    return config.get(key, default)