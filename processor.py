import json
import time
from decimal import Decimal
from typing import Dict, Any, Optional

def format_crypto_amount(amount: float, precision: int = 8) -> str:
    """Converts float to fixed precision string for exchange APIs."""
    return f"{Decimal(str(amount)):.{precision}f}"

def calculate_profit_margin(buy_price: float, sell_price: float) -> float:
    """Calculates percentage difference between two price points."""
    if buy_price <= 0:
        return 0.0
    return ((sell_price - buy_price) / buy_price) * 100

def validate_order_payload(data: Dict[str, Any]) -> bool:
    """Checks if payload contains essential order keys."""
    required = {'symbol', 'side', 'amount', 'price'}
    return all(key in data for key in required)

def log_trade_event(symbol: str, message: str) -> None:
    """Appends formatted trade event to console output."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] TRADE [{symbol.upper()}]: {message}")

def safe_json_load(raw_data: str) -> Optional[Dict[str, Any]]:
    """Safely parses JSON strings with error handling."""
    try:
        return json.loads(raw_data)
    except (json.JSONDecodeError, TypeError):
        return None