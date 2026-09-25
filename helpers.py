import time
import decimal
from typing import Union

def format_amount(amount: Union[float, str, decimal.Decimal], precision: int = 8) -> str:
    """Standardizes crypto values to specified decimal precision."""
    val = decimal.Decimal(str(amount))
    return format(val.quantize(decimal.Decimal(f'1.{"0" * precision}')), 'f')

def get_unix_timestamp() -> int:
    """Current server-side epoch time in seconds."""
    return int(time.time())

def calculate_fee(amount: float, rate: float) -> float:
    """Multiplicative fee calculation for trade orders."""
    return float(amount) * rate

def validate_ticker(ticker: str) -> bool:
    """Ensures ticker format complies with standard pairs."""
    if not isinstance(ticker, str) or '_' not in ticker:
        return False
    return ticker.isupper()

def retry_operation(func, max_attempts: int = 3, delay: float = 1.0):
    """Basic exponential backoff wrapper for API calls."""
    for i in range(max_attempts):
        try:
            return func()
        except Exception:
            if i == max_attempts - 1:
                raise
            time.sleep(delay * (2 ** i))
