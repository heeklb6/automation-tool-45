import os
from typing import Dict, Any

class Config:
    """Configuration manager for the crypto automation tool."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.api_key: str = os.getenv("CRYPTO_API_KEY", "")
        self.timeout: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
        self.base_url: str = "https://api.exchange.com/v1"

    def get_headers(self) -> Dict[str, str]:
        """Return authentication headers for exchange requests."""
        return {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    @classmethod
    def validate(cls, settings: Dict[str, Any]) -> bool:
        """Validate configuration dictionary structure."""
        required_keys = ["api_key", "timeout"]
        return all(key in settings for key in required_keys)

DEFAULT_CONFIG: Dict[str, Any] = {
    "api_key": "",
    "timeout": 30,
    "retries": 3
}