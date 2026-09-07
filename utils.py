import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("automation_tool.utils")

def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise e
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {attempt_delay:.1f}s..."
                    )
                    time.sleep(attempt_delay)
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator