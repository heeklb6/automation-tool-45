import json
import os
from typing import Any, Dict

# Default settings for the crypto automation tool
DEFAULTS = {
    "api_key": "",
    "api_secret": "",
    "base_url": "https://api.binance.com",
    "trading_pair": "BTCUSDT",
    "trade_amount": 0.001,
    "stop_loss_percent": 2.0,
    "take_profit_percent": 5.0,
    "max_retries": 5,
    "log_level": "INFO"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Load config from JSON file with defaults and env overrides."""
    config = DEFAULTS.copy()
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                if isinstance(loaded, dict):
                    config.update(loaded)
        except Exception as e:
            print(f"Config load warning: {e}")
    # Apply environment variable overrides
    for key, default in DEFAULTS.items():
        env_var = f"AUTO_{key.upper()}"
        if env_var in os.environ:
            val = os.environ[env_var]
            if isinstance(default, bool):
                config[key] = val.lower() in ["true", "1", "yes"]
            elif isinstance(default, int):
                config[key] = int(val)
            elif isinstance(default, float):
                config[key] = float(val)
            else:
                config[key] = val
    return config

# To use: from constants import load_config
# config = load_config()