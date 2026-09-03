import time
import decimal
from typing import Union

def format_crypto_amount(amount: Union[float, str, decimal.Decimal], precision: int = 8) -> str:
    """Normalize crypto amounts to string with defined precision."""
    val = decimal.Decimal(str(amount))
    return format(val, f'.{precision}f')

def retry_on_failure(retries: int = 3, delay: float = 1.0):
    """Decorator for retrying operations on transient network issues."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay * (2 ** i))
            raise last_exception
        return wrapper
    return decorator

def validate_ticker(ticker: str) -> bool:
    """Ensure ticker follows standard uppercase crypto format."""
    return bool(ticker and ticker.isupper() and 2 <= len(ticker) <= 10)

def get_timestamp_ms() -> int:
    """Generate current epoch time in milliseconds for API signatures."""
    return int(time.time() * 1000)