import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay * attempt)
            logger.error(f"Function {func.__name__} failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=2.0)
def fetch_price_data(symbol: str):
    """Example function for fetching crypto pricing."""
    # Placeholder for network request logic
    return {"symbol": symbol, "price": 0.0}
