from typing import List, Dict, Optional
import hashlib
import hmac

def generate_signature(api_secret: str, payload: str) -> str:
    """Creates an HMAC SHA256 signature for crypto API requests."""
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def format_order_data(symbol: str, quantity: float, price: float) -> Dict[str, str]:
    """Standardizes order parameters for exchange interaction."""
    return {
        "symbol": symbol.upper(),
        "qty": str(quantity),
        "price": str(price),
        "type": "limit"
    }

def calculate_portfolio_value(balances: List[Dict[str, float]], prices: Dict[str, float]) -> float:
    """Calculates total portfolio value in USD based on current market rates."""
    total_value = 0.0
    for asset in balances:
        symbol = asset.get('symbol', '')
        amount = asset.get('amount', 0.0)
        price = prices.get(symbol, 0.0)
        total_value += amount * price
    return total_value

def validate_ticker(ticker: str) -> bool:
    """Basic validation check for crypto trading pairs."""
    if not ticker or len(ticker) < 3:
        return False
    return ticker.isalnum()