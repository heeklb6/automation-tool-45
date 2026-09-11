import hmac
import hashlib
import time
from typing import Dict

def generate_hmac_signature(secret: str, payload: str) -> str:
    """Generate a SHA256 HMAC signature for API authentication."""
    byte_key = bytes(secret, 'utf-8')
    message = bytes(payload, 'utf-8')
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest()

def prepare_signed_headers(api_key: str, secret: str, payload: str) -> Dict[str, str]:
    """Create request headers with a timestamp and HMAC signature."""
    timestamp = str(int(time.time() * 1000))
    signature_payload = f"{timestamp}{payload}"
    signature = generate_hmac_signature(secret, signature_payload)
    return {
        "X-API-KEY": api_key,
        "X-SIGNATURE": signature,
        "X-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }

def format_crypto_amount(value: float, precision: int = 8) -> str:
    """Format a float amount to a specific precision without scientific notation."""
    formatted = f"{value:.{precision}f}"
    if '.' in formatted:
        formatted = formatted.rstrip('0').rstrip('.')
    return formatted if formatted != "" else "0"