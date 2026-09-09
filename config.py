import os
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    API_KEY: str = os.getenv("CRYPTO_API_KEY", "")
    API_SECRET: str = os.getenv("CRYPTO_API_SECRET", "")
    BASE_URL: str = "https://api.exchange.com/v1"
    TIMEOUT: int = 30
    MAX_RETRIES: int = 3

def load_config() -> AppConfig:
    """Initializes application configuration from environment variables."""
    return AppConfig(
        API_KEY=os.getenv("CRYPTO_API_KEY", ""),
        API_SECRET=os.getenv("CRYPTO_API_SECRET", ""),
        BASE_URL=os.getenv("BASE_URL", "https://api.exchange.com/v1"),
        TIMEOUT=int(os.getenv("REQUEST_TIMEOUT", "30")),
        MAX_RETRIES=int(os.getenv("MAX_RETRIES", "3"))
    )

# Global configuration instance for cross-module usage
settings = load_config()