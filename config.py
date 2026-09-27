import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "rpc_url": "https://eth-mainnet.g.alchemy.com/v2/demo",
    "exchange": "binance",
    "trading_pair": "BTC/USDT",
    "max_slippage_pct": 0.5,
    "gas_limit": 21000,
    "request_timeout_sec": 10,
    "enable_paper_trading": True,
    "max_position_size_usd": 1000.0,
}


def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file, merging with default values.

    Environment variables override loaded settings if present.
    """
    config = DEFAULT_CONFIG.copy()
    config_path = Path(filepath)

    if config_path.is_file():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as err:
            print(f"Warning: Failed to parse {filepath}, using defaults. Error: {err}")

    # Override settings from environment variables if set
    env_mappings = {
        "CRYPTO_RPC_URL": "rpc_url",
        "EXCHANGE_NAME": "exchange",
        "TRADING_PAIR": "trading_pair",
        "PAPER_TRADING": "enable_paper_trading",
    }

    for env_var, config_key in env_mappings.items():
        if env_var in os.environ:
            val = os.environ[env_var]
            if isinstance(config[config_key], bool):
                config[config_key] = val.lower() in ("true", "1", "yes")
            elif isinstance(config[config_key], float):
                config[config_key] = float(val)
            elif isinstance(config[config_key], int):
                config[config_key] = int(val)
            else:
                config[config_key] = val

    return config