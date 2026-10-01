import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "rpc_url": "https://bsc-dataseed.binance.org/",
    "gas_limit": 200000,
    "retry_attempts": 3,
    "log_level": "INFO"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with hardcoded defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Config load error, using defaults: {e}")
    
    return config

def get_rpc_url() -> str:
    """Access the configured rpc endpoint."""
    return load_config().get("rpc_url", DEFAULT_CONFIG["rpc_url"])

if __name__ == "__main__":
    # Demo of configuration loading logic
    current_cfg = load_config()
    print(f"Loaded settings: {current_cfg}")