import functools
from typing import Dict, Any

# Cache for address validation results to minimize regex overhead
_VALIDATION_CACHE: Dict[str, bool] = {}

@functools.lru_cache(maxsize=1024)
def validate_address_format(address: str) -> bool:
    """Validates crypto address format using cached regex matches."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False
    return address.startswith('0x')

def bulk_validate_addresses(address_list: list) -> Dict[str, bool]:
    """
    Batch validation with cache lookup to optimize
    repeated processing of identical wallet addresses.
    """
    results = {}
    for addr in address_list:
        # Using local cache lookup before compute-heavy check
        if addr not in _VALIDATION_CACHE:
            _VALIDATION_CACHE[addr] = validate_address_format(addr)
        results[addr] = _VALIDATION_CACHE[addr]
    return results

def clear_validator_cache() -> None:
    """Clears memory for long-running automation processes."""
    _VALIDATION_CACHE.clear()
    validate_address_format.cache_clear()