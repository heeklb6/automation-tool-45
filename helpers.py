import time
import logging
from typing import Callable, Any

# Configure logger for automation-tool-45
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-45')

def retry_operation(func: Callable, retries: int = 3, delay: int = 2) -> Any:
    """Execute function with retry mechanism for transient errors."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}")
            if i == retries - 1:
                raise e
            time.sleep(delay)

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Format float to crypto-standard string representation."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def calculate_profit_percentage(initial: float, final: float) -> float:
    """Calculate return percentage between two values."""
    if initial == 0:
        return 0.0
    return ((final - initial) / initial) * 100

def validate_pair(pair: str) -> bool:
    """Verify trading pair format e.g. BTCUSDT."""
    return isinstance(pair, str) and len(pair) >= 6 and pair.isupper()