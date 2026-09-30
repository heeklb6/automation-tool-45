import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Format raw floats into standardized crypto string notation."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def validate_order_params(params: Dict[str, Any]) -> bool:
    """Ensure required fields exist in order payload."""
    required = ['symbol', 'side', 'type', 'quantity']
    return all(key in params for key in required)

def retry_operation(func, retries: int = 3, delay: float = 1.0):
    """Execution wrapper for transient network failures."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay * (2 ** attempt))
    raise last_exception

def calculate_position_size(balance: float, risk_pct: float, price: float) -> float:
    """Size calculation based on risk tolerance."""
    return (balance * risk_pct) / price