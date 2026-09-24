from typing import Final, Dict, List

# Network identifiers for blockchain interaction
MAINNET_CHAIN_ID: Final[int] = 1
TESTNET_CHAIN_ID: Final[int] = 11155111

# Trading execution constraints
MAX_RETRIES: Final[int] = 3
REQUEST_TIMEOUT: Final[float] = 30.0

# Supported asset identifiers
SUPPORTED_TOKENS: Final[List[str]] = ["BTC", "ETH", "SOL"]

# API threshold settings in milliseconds
RATE_LIMIT_DELAY: Final[int] = 500

# Mapping for fee calculation tiers
FEE_TIERS: Final[Dict[str, float]] = {
    "low": 0.001,
    "medium": 0.005,
    "high": 0.01
}

def get_chain_name(chain_id: int) -> str:
    """Return the human-readable name for a given network ID."""
    mapping: Dict[int, str] = {
        MAINNET_CHAIN_ID: "mainnet",
        TESTNET_CHAIN_ID: "sepolia"
    }
    return mapping.get(chain_id, "unknown")
