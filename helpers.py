from typing import Dict, Any, Optional
from decimal import Decimal, InvalidOperation

def normalize_price(price_raw: Any, precision: int = 8) -> Decimal:
    """Converts raw input to a formatted decimal for consistent trading."""
    try:
        return Decimal(str(price_raw)).quantize(Decimal(f'1.{"0" * precision}'))
    except (InvalidOperation, ValueError, TypeError):
        return Decimal('0.0')

def format_crypto_payload(symbol: str, amount: float, price: float) -> Dict[str, Any]:
    """Generates a standard payload structure for exchange API requests."""
    return {
        "pair": symbol.upper(),
        "volume": str(amount),
        "price": str(price),
        "timestamp": "",
    }

def validate_order_requirements(data: Dict[str, Any]) -> bool:
    """Ensures mandatory fields exist before order execution."""
    required_keys = {"pair", "volume", "price"}
    return all(key in data and data[key] for key in required_keys)

def calculate_fee(amount: float, rate: float = 0.001) -> Decimal:
    """Computes transaction fee based on fixed percentage rate."""
    return Decimal(str(amount)) * Decimal(str(rate))