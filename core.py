import time
import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API authentication."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_price(amount: float, precision: int = 8) -> str:
    """Formats crypto price to fixed point string."""
    return f"{amount:.{precision}f}"

def retry_on_failure(func, retries: int = 3, delay: float = 1.0):
    """Retry logic wrapper for network-dependent functions."""
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if i == retries - 1:
                raise e
            time.sleep(delay * (2 ** i))

def sanitize_order_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from API order payloads."""
    return {k: v for k, v in data.items() if v is not None}