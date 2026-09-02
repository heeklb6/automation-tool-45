import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULTS: Dict[str, Any] = {
    "api_key": "",
    "api_secret": "",
    "exchange": "binance",
    "network": "mainnet",
    "trading_pairs": ["BTC/USDT"],
    "max_position_size": 1000,
    "risk_percentage": 2.0,
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "dry_run": True,
}

class ConfigLoader:
    """Loads and manages configuration with defaults for crypto automation."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = DEFAULTS.copy()
        self.load()

    def load(self) -> None:
        """Load config from file if exists, merging with defaults."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                if isinstance(user_config, dict):
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError, OSError) as e:
                print(f"Config load error: {e}. Using defaults only.")

        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        """Apply environment variable overrides where applicable."""
        for key, default_value in DEFAULTS.items():
            env_var = f"AUTO_{key.upper()}"
            if env_var in os.environ:
                env_value = os.environ[env_var]
                if isinstance(default_value, bool):
                    self.config[key] = env_value.lower() in ("true", "1", "yes")
                elif isinstance(default_value, int):
                    try:
                        self.config[key] = int(env_value)
                    except ValueError:
                        pass
                elif isinstance(default_value, float):
                    try:
                        self.config[key] = float(env_value)
                    except ValueError:
                        pass
                else:
                    self.config[key] = env_value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get a config value with optional default."""
        return self.config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """Return the full configuration dictionary."""
        return self.config.copy()

    def save(self) -> None:
        """Save current config to file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2)
        except IOError as e:
            print(f"Failed to save config: {e}")