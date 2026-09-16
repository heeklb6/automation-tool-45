from typing import Dict, Any, Optional
import hashlib
import hmac

def calculate_hmac_signature(api_secret: str, payload: str) -> str:
    """
    Generates an HMAC SHA256 signature for crypto API requests.

    :param api_secret: The private key for authentication
    :param payload: The query string or body to sign
    :return: Hexadecimal signature string
    """
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_order_data(symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
    """
    Normalizes order data into a standard exchange-compatible dictionary.

    :param symbol: Trading pair (e.g., BTCUSDT)
    :param side: BUY or SELL
    :param amount: Quantity to trade
    :param price: Execution price
    :return: Dictionary containing formatted order details
    """
    return {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "quantity": str(amount),
        "price": str(price),
        "type": "LIMIT"
    }

def parse_env_variable(value: Optional[str], default: str) -> str:
    """
    Safely retrieves environment configuration values.

    :param value: Raw environment variable string
    :param default: Fallback value if input is None or empty
    :return: Valid configuration string
    """
    return value if value and len(value) > 0 else default