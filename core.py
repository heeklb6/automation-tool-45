import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-45')

def retry_network_call(retries: int = 3, delay: float = 1.5):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(retries=3)
def fetch_crypto_price(ticker: str) -> float:
    """Example network-bound function to fetch price data."""
    # Placeholder for actual network request logic
    return 0.0