import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "exchange": "binance",
    "api_key": "",
    "symbol": "BTC/USDT",
    "retry_limit": 3,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file with hardcoded defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load config at {path}: {e}")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """Ensures mandatory fields exist in configuration."""
    required = ["api_key", "symbol"]
    return all(config.get(key) for key in required)

if __name__ == "__main__":
    # Example usage for crypto automation startup
    active_config = load_config()
    if not validate_config(active_config):
        print("Configuration incomplete, check api_key and symbol.")