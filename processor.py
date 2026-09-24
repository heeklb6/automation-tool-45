import json
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional

def normalize_crypto_data(data: Dict) -> Dict:
    """Standardizes incoming crypto market data formats."""
    required_fields = ['symbol', 'price', 'volume']
    
    # ensure basic data integrity
    if not all(k in data for k in required_fields):
        raise ValueError(f"Missing required fields in data: {data}")

    try:
        return {
            "symbol": str(data['symbol']).upper(),
            "price": float(Decimal(str(data['price'])).quantize(Decimal('0.00000001')),
            "volume": float(Decimal(str(data['volume'])).quantize(Decimal('0.00000001'))),
            "timestamp": data.get('timestamp')
        }
    except (ValueError, TypeError) as e:
        raise ValueError(f"Data transformation error: {e}")

def batch_process_prices(items: List[Dict]) -> List[Dict]:
    """Processes list of raw tick data for storage."""
    processed = []
    for item in items:
        try:
            processed.append(normalize_crypto_data(item))
        except ValueError:
            continue
    return processed

def calculate_value(price: float, amount: float) -> str:
    """Precise calculation of position value in USD."""
    val = Decimal(str(price)) * Decimal(str(amount))
    return str(val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))