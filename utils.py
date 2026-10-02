import re
from decimal import Decimal, ROUND_DOWN

def to_fixed_precision(amount: float, decimals: int) -> str:
    """Converts float amount to a string with exact decimal precision, avoiding scientific notation."""
    dec = Decimal(str(amount))
    precision_str = '1.' + '0' * decimals if decimals > 0 else '1'
    quantized = dec.quantize(Decimal(precision_str), rounding=ROUND_DOWN)
    return str(quantized)

def calculate_slippage_price(base_price: float, slippage_pct: float, is_buy: bool = True) -> float:
    """Calculates the limit price considering a specific slippage percentage."""
    factor = 1 + (slippage_pct / 100.0) if is_buy else 1 - (slippage_pct / 100.0)
    return round(base_price * factor, 8)

def is_valid_evm_address(address: str) -> bool:
    """Validates if the provided string is a hex-encoded EVM address."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))

def convert_to_wei(amount: float, decimals: int = 18) -> int:
    """Converts a token amount to its smallest integer unit (Wei equivalent)."""
    dec_amount = Decimal(str(amount))
    multiplier = Decimal(10 ** decimals)
    return int(dec_amount * multiplier)
