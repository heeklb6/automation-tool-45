import time
import functools
import logging
from typing import Callable, Any

# Configure logger for automation-tool-45 network operations
logger = logging.getLogger('automation-tool-45')

class NetworkError(Exception):
    """Custom exception for crypto API connectivity issues."""
    pass

def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator for retrying network operations with exponential backoff.
    
    Args:
        max_attempts: Total number of attempts including initial try
        delay: Base sleep duration between retries in seconds
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))
            
            logger.error(f"Final attempt failed after {max_attempts} retries.")
            raise NetworkError(f"Failed after {max_attempts} attempts: {last_exception}")
        return wrapper
    return decorator