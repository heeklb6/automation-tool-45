from typing import Dict, Final, List

# Network configuration and chain IDs
SUPPORTED_CHAINS: Final[Dict[str, int]] = {
    "ethereum": 1,
    "arbitrum": 42161,
    "optimism": 10,
    "polygon": 137,
    "bsc": 56,
}

# Default API endpoints for fallback RPC connections
DEFAULT_RPC_URLS: Final[Dict[int, str]] = {
    1: "https://cloudflare-eth.com",
    42161: "https://arb1.arbitrum.io/rpc",
    10: "https://mainnet.optimism.io",
    137: "https://polygon-rpc.com",
    56: "https://bsc-dataseed.binance.org",
}

# Common ERC-20 Token Addresses (Ethereum Mainnet)
ETHEREUM_TOKENS: Final[Dict[str, str]] = {
    "WETH": "0xC02aaA39b223FE8D0A0e5C4F27ead9083C756Cc2",
    "USDC": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "USDT": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
}

# Transaction defaults
DEFAULT_SLIPPAGE_BPS: Final[int] = 50  # 0.5% slippage representation in basis points
DEFAULT_GAS_LIMIT: Final[int] = 250000
TX_TIMEOUT_SECONDS: Final[int] = 120

# HTTP Connection settings
MAX_RETRIES: Final[int] = 3
RETRY_BACKOFF_FACTOR: Final[float] = 1.5


def get_supported_chain_names() -> List[str]:
    """Retrieve a list of supported blockchain network names.

    Returns:
        List[str]: A list of lowercase network names.
    """
    return list(SUPPORTED_CHAINS.keys())
