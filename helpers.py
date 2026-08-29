import re
from datetime import datetime
import hashlib

def to_wei(amount: float, unit: str = "ether") -> int:
    """Convert amount to smallest unit like wei."""
    conversion_rates = {
        "wei": 1,
        "gwei": 1_000_000_000,
        "ether": 1_000_000_000_000_000_000,
        "satoshi": 1,
        "bitcoin": 100_000_000
    }
    if unit not in conversion_rates:
        raise ValueError("Unsupported unit")
    rate = conversion_rates[unit]
    return int(amount * rate)

def from_wei(amount: int, unit: str = "ether") -> float:
    """Convert from smallest unit back to standard."""
    conversion_rates = {
        "wei": 1,
        "gwei": 1_000_000_000,
        "ether": 1_000_000_000_000_000_000,
        "satoshi": 1,
        "bitcoin": 100_000_000
    }
    if unit not in conversion_rates:
        raise ValueError("Unsupported unit")
    rate = conversion_rates[unit]
    return amount / rate

def validate_address(address: str, chain: str = "ethereum") -> bool:
    """Validate address for given chain."""
    if chain == "ethereum":
        pattern = r"^0x[0-9a-fA-F]{40}$"
        return bool(re.match(pattern, address))
    elif chain == "bitcoin":
        if len(address) < 26 or len(address) > 35:
            return False
        return address[0] in "13" and bool(re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address))
    return False

def calculate_gas_fee(gas_limit: int, gas_price_gwei: float) -> float:
    """Calculate gas fee in ether."""
    gas_price_wei = gas_price_gwei * 1_000_000_000
    total_wei = gas_limit * gas_price_wei
    return total_wei / 1_000_000_000_000_000_000

def get_current_timestamp() -> int:
    """Return current unix timestamp."""
    return int(datetime.now().timestamp())

def format_crypto_amount(amount: float, decimals: int = 8) -> str:
    """Format amount with specified decimals."""
    return f"{amount:.{decimals}f}"

def hash_transaction(tx_data: str) -> str:
    """Generate hash for transaction data."""
    return hashlib.sha256(tx_data.encode('utf-8')).hexdigest()

def is_valid_amount(amount: float) -> bool:
    """Check if amount is valid positive number."""
    return isinstance(amount, (int, float)) and amount > 0
