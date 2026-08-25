import os
import json
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CryptoConfig:
    """Configuration class for crypto automation tool."""
    api_key: str
    api_secret: str
    exchange: str = "binance"
    trading_pair: str = "BTC/USDT"
    max_position_size: float = 0.1
    timeout: int = 30

def load_config(config_path: str = "config.json") -> CryptoConfig:
    """Load crypto configuration from a JSON file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, "r") as file:
        data = json.load(file)
    
    return CryptoConfig(
        api_key=data.get("api_key", ""),
        api_secret=data.get("api_secret", ""),
        exchange=data.get("exchange", "binance"),
        trading_pair=data.get("trading_pair", "BTC/USDT"),
        max_position_size=float(data.get("max_position_size", 0.1)),
        timeout=int(data.get("timeout", 30))
    )

def save_config(config: CryptoConfig, config_path: str = "config.json") -> None:
    """Save crypto configuration to a JSON file."""
    data = {
        "api_key": config.api_key,
        "api_secret": config.api_secret,
        "exchange": config.exchange,
        "trading_pair": config.trading_pair,
        "max_position_size": config.max_position_size,
        "timeout": config.timeout
    }
    with open(config_path, "w") as file:
        json.dump(data, file, indent=2)

def get_config_from_env() -> CryptoConfig:
    """Retrieve configuration from environment variables for crypto ops."""
    return CryptoConfig(
        api_key=os.getenv("CRYPTO_API_KEY", ""),
        api_secret=os.getenv("CRYPTO_API_SECRET", ""),
        exchange=os.getenv("CRYPTO_EXCHANGE", "binance"),
        trading_pair=os.getenv("CRYPTO_TRADING_PAIR", "BTC/USDT"),
        max_position_size=float(os.getenv("CRYPTO_MAX_POSITION", "0.1")),
        timeout=int(os.getenv("CRYPTO_TIMEOUT", "30"))
    )

def validate_config(config: CryptoConfig) -> bool:
    """Validate essential fields in the crypto configuration."""
    if not config.api_key or len(config.api_key) < 10:
        return False
    if not config.api_secret or len(config.api_secret) < 10:
        return False
    if config.exchange not in ["binance", "coinbase", "kraken"]:
        return False
    if config.max_position_size <= 0 or config.max_position_size > 1:
        return False
    return True

def merge_configs(base: CryptoConfig, override: Dict[str, Any]) -> CryptoConfig:
    """Merge base config with override dictionary for flexible updates."""
    merged = {
        "api_key": override.get("api_key", base.api_key),
        "api_secret": override.get("api_secret", base.api_secret),
        "exchange": override.get("exchange", base.exchange),
        "trading_pair": override.get("trading_pair", base.trading_pair),
        "max_position_size": override.get("max_position_size", base.max_position_size),
        "timeout": override.get("timeout", base.timeout)
    }
    return CryptoConfig(**merged)