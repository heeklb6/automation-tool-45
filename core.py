import decimal
from typing import Dict, Optional

def sanitize_price(raw_price: any) -> decimal.Decimal:
    """Converts raw API data to a standard Decimal type."""
    try:
        return decimal.Decimal(str(raw_price))
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0.0')

def calculate_position_size(balance: decimal.Decimal, risk_pct: float, stop_loss_dist: decimal.Decimal) -> decimal.Decimal:
    """Calculates position size based on equity risk percentage."""
    if stop_loss_dist <= 0:
        return decimal.Decimal('0')
    
    risk_amount = balance * decimal.Decimal(str(risk_pct))
    return risk_amount / stop_loss_dist

def format_crypto_pair(base: str, quote: str) -> str:
    """Standardizes ticker formatting for exchanges."""
    return f"{base.upper()}/{quote.upper()}"

def parse_order_response(data: Dict) -> Optional[Dict]:
    """Extracts core fields from raw exchange JSON responses."""
    if not data or 'id' not in data:
        return None
    
    return {
        'order_id': data.get('id'),
        'status': data.get('status', 'unknown'),
        'filled': sanitize_price(data.get('filled_size', 0))
    }