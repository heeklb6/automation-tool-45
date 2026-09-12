import time
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry network-bound operations with exponential backoff."""
    def decorator(func: Callable):
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@with_retry(retries=3, delay=0.5)
def fetch_price_data(symbol: str):
    """Simulated network call to crypto exchange API."""
    # Example: request.get(f"https://api.exchange.com/v1/ticker/{symbol}")
    print(f"Fetching price for {symbol}...")
    # Simulate network instability
    raise ConnectionError("API unreachable")

if __name__ == "__main__":
    try:
        fetch_price_data("BTC")
    except Exception:
        print("Network operation failed after retries.")