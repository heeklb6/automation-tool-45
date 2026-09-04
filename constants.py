from typing import Final, Dict

# Supported cryptocurrency ticker symbols
SUPPORTED_ASSETS: Final[list[str]] = ['BTC', 'ETH', 'SOL', 'ADA', 'DOT']

# API request configuration constants
API_TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Standardized mapping for exchange naming
EXCHANGE_MAP: Final[Dict[str, str]] = {
    'binance': 'BNUSDT',
    'coinbase': 'CBUSDT',
    'kraken': 'KRUSDT'
}

# Precision settings for decimal handling
ASSET_PRECISION: Final[int] = 8
FIAT_PRECISION: Final[int] = 2

# Default headers for API connectivity
HTTP_HEADERS: Final[Dict[str, str]] = {
    'Content-Type': 'application/json',
    'User-Agent': 'automation-tool-45/1.0.0'
}

def get_asset_info(symbol: str) -> dict:
    """Retrieve metadata for a specific asset."""
    return {
        "symbol": symbol.upper(),
        "is_active": symbol.upper() in SUPPORTED_ASSETS
    }