import re
from typing import Any, Dict, Optional, Tuple


def is_valid_eth_address(address: str) -> bool:
    """Check if the provided string is a valid Ethereum wallet address."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))


def is_valid_btc_address(address: str) -> bool:
    """Check basic format for Bitcoin Legacy, SegWit, or Bech32 addresses."""
    if not isinstance(address, str):
        return False
    pattern = r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-0-9]{8,87})$"
    return bool(re.match(pattern, address))


def validate_trade_order(order: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate incoming crypto trade order data before execution."""
    required_fields = ["symbol", "side", "amount", "price"]
    for field in required_fields:
        if field not in order:
            return False, f"Missing required field: {field}"

    if str(order["side"]).upper() not in ["BUY", "SELL"]:
        return False, "Invalid order side, must be BUY or SELL"

    if not isinstance(order["amount"], (int, float)) or order["amount"] <= 0:
        return False, "Amount must be a positive number"

    if not isinstance(order["price"], (int, float)) or order["price"] <= 0:
        return False, "Price must be a positive number"

    symbol_pattern = r"^[A-Z0-9]{2,10}/[A-Z0-9]{2,10}$"
    if not re.match(symbol_pattern, str(order["symbol"]).upper()):
        return False, "Invalid symbol format (expected BASE/QUOTE)"

    return True, None
