import re

class InputValidator:
    """Utility to ensure crypto input integrity."""

    @staticmethod
    def is_valid_address(address: str) -> bool:
        """Check if address matches standard hex patterns."""
        if not isinstance(address, str) or len(address) < 26:
            return False
        return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

    @staticmethod
    def is_valid_amount(amount: str) -> bool:
        """Verify numerical format for crypto quantities."""
        try:
            value = float(amount)
            return value > 0
        except (ValueError, TypeError):
            return False

def validate_payload(data: dict) -> bool:
    """
    Main entry point for processing loop validation.
    Expects keys: 'address' and 'amount'.
    """
    address = data.get('address')
    amount = data.get('amount')

    if not InputValidator.is_valid_address(address):
        return False
    
    if not InputValidator.is_valid_amount(amount):
        return False

    return True