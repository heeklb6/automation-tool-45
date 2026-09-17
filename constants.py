import math
from typing import Final, Dict

# Network timeout settings for high-frequency trading
TIMEOUT_CONNECT: Final[float] = 2.5
TIMEOUT_READ: Final[float] = 5.0

# Rate limiting buffer based on exchange constraints
RATE_LIMIT_BUFFER: Final[int] = 100
MAX_CONCURRENT_REQUESTS: Final[int] = 50

# Caching performance configurations
CACHE_TTL_SECONDS: Final[int] = 300
CACHE_MAX_SIZE: Final[int] = 1024

# Calculation precision for crypto math operations
DECIMAL_PRECISION: Final[int] = 18
DEFAULT_SLIPPAGE: Final[float] = 0.005

# Optimized operational status mapping
STATUS_MAP: Final[Dict[int, str]] = {
    0: "PENDING",
    1: "EXECUTING",
    2: "COMPLETED",
    3: "FAILED",
    4: "CANCELLED"
}

def get_performance_thresholds(volatility: float) -> float:
    """Calculates dynamic threshold for latency mitigation."""
    base_threshold = 0.05
    return base_threshold * math.exp(volatility)
