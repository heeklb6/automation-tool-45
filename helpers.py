import time
import hashlib
import hmac
from typing import Dict, Any

def generate_signature(api_secret: str, payload: str) -> str:
    """Generates HMAC-SHA256 signature for API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def get_timestamp_ms() -> int:
    """Returns current unix timestamp in milliseconds."""
    return int(time.time() * 1000)

def format_price(amount: float, precision: int = 8) -> str:
    """Formats float to crypto-standard string representation."""
    return f"{amount:.{precision}f}".rstrip('0').rstrip('.')

def sanitize_order_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values and sorts keys for API consistency."""
    return {k: v for k, v in sorted(params.items()) if v is not None}

def retry_operation(func, retries: int = 3, delay: float = 1.0):
    """Simple wrapper for network-dependent operations."""
    for i in range(retries):
        try:
            return func()
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay * (2 ** i))
    return None