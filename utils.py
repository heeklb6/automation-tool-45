import time
import functools
import logging
from typing import Callable, Any, Tuple, Type
import requests

logger = logging.getLogger(__name__)

def retry_network_call(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[Type[BaseException], ...] = (requests.RequestException, TimeoutError)
) -> Callable:
    """
    Decorator that retries network operations with exponential backoff.
    Targeted for crypto node RPC calls and exchange API interactions.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            delay = 1.0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(
                            "Max retries (%d) exceeded for network operation %s. Final error: %s",
                            max_retries,
                            func.__name__,
                            err
                        )
                        raise
                    
                    logger.warning(
                        "Network call %s failed (attempt %d/%d): %s. Retrying in %.2fs...",
                        func.__name__,
                        retries,
                        max_retries,
                        err,
                        delay
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator

@retry_network_call(max_retries=4, backoff_factor=2.0)
def fetch_market_depth(endpoint_url: str, symbol: str) -> dict:
    """Fetch orderbook depth data for a given cryptocurrency trading pair."""
    response = requests.get(endpoint_url, params={"symbol": symbol}, timeout=5)
    response.raise_for_status()
    return response.json()
