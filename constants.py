import os
from decimal import Decimal

# Network and exchange endpoints
API_BASE_URL = "https://api.exchange.com/v3"
WS_BASE_URL = "wss://ws.exchange.com/v3"

# Supported trading pairs
TRADING_PAIRS = {
    "BTC/USDT": "BTCUSDT",
    "ETH/USDT": "ETHUSDT",
    "SOL/USDT": "SOLUSDT"
}

# Decimal precision settings
PRICE_PRECISION = 8
AMOUNT_PRECISION = 6
FEE_RATE = Decimal("0.001")

# Order types
ORDER_TYPE_LIMIT = "LIMIT"
ORDER_TYPE_MARKET = "MARKET"

# Timeouts in seconds
REQUEST_TIMEOUT = 10
WS_RECONNECT_INTERVAL = 5

# Default log path
LOG_FILE = "automation-tool-45.log"

# Minimum trade amounts
MIN_ORDER_VALUE_USDT = Decimal("10.0")

# Supported order statuses
STATUS_OPEN = "OPEN"
STATUS_FILLED = "FILLED"
STATUS_CANCELED = "CANCELED"
STATUS_REJECTED = "REJECTED"