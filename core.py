import decimal
from typing import Dict, Union

def normalize_crypto_amount(amount: Union[str, float, int], precision: int = 8) -> decimal.Decimal:
    """Converts crypto amount strings to precise decimal objects."""
    context = decimal.Context(prec=precision, rounding=decimal.ROUND_HALF_UP)
    return context.create_decimal(str(amount))

def format_order_payload(symbol: str, side: str, price: float, quantity: float) -> Dict:
    """Constructs standard dictionary payload for exchange APIs."""
    return {
        "symbol": symbol.upper(),
        "side": side.lower(),
        "type": "limit",
        "price": str(price),
        "quantity": str(quantity),
        "timestamp": None
    }

def calculate_position_size(balance: float, risk_percentage: float, stop_loss_pct: float) -> float:
    """Calculates trade size based on account risk management."""
    if not (0 < risk_percentage <= 100) or stop_loss_pct <= 0:
        return 0.0
    risk_amount = balance * (risk_percentage / 100)
    return risk_amount / (stop_loss_pct / 100)

def sanitize_symbol(symbol: str) -> str:
    """Standardizes trading pair formats by removing separators."""
    return symbol.replace('/', '').replace('_', '').upper()