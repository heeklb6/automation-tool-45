import time
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute function with simple exponential backoff."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay * (2 ** attempt))
    raise last_exception

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Normalize float values to string for API payloads."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def validate_ticker(ticker: str) -> bool:
    """Check if ticker string meets standard exchange format."""
    if not ticker or '_' not in ticker:
        return False
    base, quote = ticker.split('_')
    return base.isalnum() and quote.isalnum()

def get_timestamp_ms() -> int:
    """Current unix epoch in milliseconds for exchange APIs."""
    return int(time.time() * 1000)