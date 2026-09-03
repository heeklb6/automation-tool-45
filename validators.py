import re
from typing import Any, Optional

# Validation patterns for crypto transaction data
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_wallet_address(address: str) -> bool:
    """Checks if string is a valid Ethereum-style wallet address."""
    return bool(ADDRESS_PATTERN.match(address))

def validate_transaction_amount(amount: Any) -> bool:
    """Ensures amount is a positive numeric value for trade processing."""
    try:
        val = float(amount)
        return val > 0
    except (TypeError, ValueError):
        return False

def sanitize_input(data: dict) -> Optional[dict]:
    """Validates fields in the input payload before processing starts."""
    address = data.get('address')
    amount = data.get('amount')

    if not address or not validate_wallet_address(address):
        return None

    if not validate_transaction_amount(amount):
        return None

    return {
        'address': address,
        'amount': float(amount)
    }