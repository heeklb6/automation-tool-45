import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.binance.com",
    "api_key": "",
    "api_secret": "",
    "trading_pairs": ["BTC/USDT", "ETH/USDT"],
    "max_slippage": 0.01,
    "enable_telemetry": True,
    "request_timeout": 30
}

class ConfigLoader:
    """Handles loading, validation, and env-override of crypto app configuration."""
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configurations from file and environment variables."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self.config.update(file_config)
            except (json.JSONDecodeError, OSError):
                # Gracefully fall back to defaults if file is corrupted
                pass

        # Environment variables override defaults and file config
        for key, default_val in DEFAULT_CONFIG.items():
            env_key = f"CRYPTO_{key.upper()}"
            env_val = os.getenv(env_key)
            if env_val is not None:
                if isinstance(default_val, bool):
                    self.config[key] = env_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    self.config[key] = int(env_val)
                elif isinstance(default_val, float):
                    self.config[key] = float(env_val)
                elif isinstance(default_val, list):
                    self.config[key] = [item.strip() for item in env_val.split(",")]
                else:
                    self.config[key] = env_val

        return self.config

    def get(self, key: str) -> Any:
        """Safe accessor for configuration values."""
        return self.config.get(key)