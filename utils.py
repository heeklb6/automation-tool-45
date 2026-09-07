import functools
import time
from typing import Callable, Any

# Cache dictionary for crypto ticker results
_CACHE = {}
_TTL = 60

def memoize_crypto_data(func: Callable) -> Callable:
    """Decorator for reducing redundant API calls in automation-tool-45."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = f"{func.__name__}:{args}:{kwargs}"
        now = time.time()

        if key in _CACHE:
            timestamp, result = _CACHE[key]
            if now - timestamp < _TTL:
                return result

        result = func(*args, **kwargs)
        _CACHE[key] = (now, result)
        return result
    return wrapper

def batch_process_trades(trades: list[dict], chunk_size: int = 100) -> list[list[dict]]:
    """Efficient generator for processing crypto trades in memory-safe chunks."""
    for i in range(0, len(trades), chunk_size):
        yield trades[i:i + chunk_size]

def normalize_pair_format(pair: str) -> str:
    """Standardize market pairs to avoid redundant data lookups."""
    return pair.replace("/", "").replace("-", "").upper()