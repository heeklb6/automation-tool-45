import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-45')

class NetworkRetryError(Exception):
    """Raised when network operations fail after max retries."""
    pass

def with_retry(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise NetworkRetryError(f"Failed after {max_retries} retries") from last_exception
        return wrapper
    return decorator