import time
import logging
import functools
import urllib.error
import urllib.request
import json
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: tuple = (urllib.error.URLError, TimeoutError, ConnectionError)
):
    """
    Decorator for retrying network operations with exponential backoff.
    Designed for crypto API endpoints prone to transient connection errors.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            delay = 1.0

            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    retries += 1
                    if retries > max_retries:
                        logger.error(f"Failed '{func.__name__}' after {max_retries} retries: {err}")
                        raise
                    
                    sleep_time = delay * (backoff_factor ** (retries - 1))
                    logger.warning(
                        f"Network error in '{func.__name__}': {err}. Retrying in {sleep_time:.2f}s ({retries}/{max_retries})"
                    )
                    time.sleep(sleep_time)

        return wrapper
    return decorator


def fetch_crypto_price(symbol: str = "BTCUSDT") -> Optional[dict]:
    """
    Fetch current ticker price from public crypto API with retries.
    """
    @retry_network_op(max_retries=3, backoff_factor=2.0)
    def _api_request() -> dict:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        req = urllib.request.Request(url, headers={"User-Agent": "automation-tool-45/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))

    try:
        return _api_request()
    except Exception as err:
        logger.error(f"Could not fetch price for {symbol}: {err}")
        return None
