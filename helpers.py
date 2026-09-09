import logging
import time
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def retry_on_failure(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator for handling transient crypto API connection issues."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay * (2 ** attempt))
            logger.error(f"Max retries reached. Final error: {last_exception}")
            raise last_exception
        return wrapper
    return decorator

def validate_wallet_address(address: str) -> bool:
    """Basic structure validation for crypto wallet strings."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.isalnum()

def safe_execute(func: Callable, default: Any = None) -> Any:
    """Generic execution wrapper for edge case safety."""
    try:
        return func()
    except Exception as e:
        logger.error(f"Execution error in {func.__name__}: {e}")
        return default