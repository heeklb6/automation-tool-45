import time
import logging
import functools
from typing import Callable, Any

# Configure logger for crypto automation tool
logger = logging.getLogger('automation-tool-45')

def retry_network_operation(retries: int = 3, delay: float = 1.0):
    """
    Decorator to implement exponential backoff for network calls
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            logger.error("Max retries reached for network operation")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(retries=3, delay=2.0)
def fetch_price_data(symbol: str):
    """
    Example network operation for crypto price lookup
    """
    # Simulate network call logic here
    pass