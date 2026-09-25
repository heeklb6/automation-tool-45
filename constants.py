from typing import Final, Dict, List

# Network identifiers for crypto operations
MAINNET: Final[str] = "mainnet"
TESTNET: Final[str] = "testnet"

# Default connection parameters
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 5

# Supported exchange identifiers
EXCHANGES: List[str] = ["binance", "kraken", "coinbase"]

# Mapping of standard asset symbols to internal IDs
ASSET_MAP: Dict[str, str] = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana"
}

def get_exchange_config(exchange: str) -> Dict[str, str]:
    """
    Retrieve basic configuration template for a specific exchange.

    Args:
        exchange: The identifier of the target exchange.

    Returns:
        A dictionary containing default API settings.
    """
    return {
        "base_url": f"https://api.{exchange}.com",
        "auth_type": "bearer"
    }