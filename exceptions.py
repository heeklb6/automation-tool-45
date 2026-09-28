import time
import functools
import logging
from typing import Callable, Any

# Configure logger for automation-tool-45 network operations
logger = logging.getLogger('automation-tool-45')

class NetworkRetryError(Exception):
    """Custom exception for persistent network failures."""
    pass

def with_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            logger.error(f"Operation failed after {max_attempts} attempts")
            raise NetworkRetryError(f"Failed after {max_attempts} attempts: {last_exception}")
        return wrapper
    return decorator