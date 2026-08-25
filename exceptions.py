"""Custom exceptions for crypto automation tool.
Implements error handling for edge cases like auth, funds, rate limits and slippage.
"""

class CryptoAutomationError(Exception):
    """Base exception for the automation tool."""
    def __init__(self, message, code=0, details=None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    def to_dict(self):
        return {"error": self.message, "code": self.code, "details": self.details}

class APIError(CryptoAutomationError):
    """API related errors."""
    pass

class AuthenticationError(APIError):
    """Invalid API authentication."""
    def __init__(self):
        super().__init__("Invalid API credentials", 401)

class InsufficientFundsError(CryptoAutomationError):
    """Not enough balance for trade."""
    def __init__(self, asset, required, available):
        msg = f"Insufficient {asset}: {required} required, {available} available"
        super().__init__(msg, 402, {"asset": asset, "required": required, "available": available})

class RateLimitError(APIError):
    """Hit rate limit."""
    def __init__(self, retry_after=60):
        super().__init__("Rate limit exceeded", 429, {"retry_after": retry_after})

class InvalidAddressError(CryptoAutomationError):
    """Bad wallet address."""
    def __init__(self, address):
        super().__init__(f"Invalid address: {address}", 400, {"address": address})

class SlippageExceededError(CryptoAutomationError):
    """Trade slippage too high."""
    def __init__(self, expected, actual):
        msg = f"Slippage exceeded: expected {expected} actual {actual}"
        super().__init__(msg, 503, {"expected": expected, "actual": actual})

class ErrorHandler:
    """Basic error handler for edge cases."""
    def __init__(self):
        self.handled = []

    def handle(self, error):
        """Return handling info based on error type."""
        if isinstance(error, InsufficientFundsError):
            action = "cancel"
            msg = "Insufficient funds - order cancelled"
        elif isinstance(error, RateLimitError):
            action = "wait"
            msg = f"Wait {error.details.get('retry_after', 60)}s"
        elif isinstance(error, SlippageExceededError):
            action = "reduce_size"
            msg = "Reduce order size to avoid slippage"
        elif isinstance(error, AuthenticationError):
            action = "re_auth"
            msg = "Re-authenticate with new keys"
        elif isinstance(error, InvalidAddressError):
            action = "fix_address"
            msg = "Provide valid wallet address"
        else:
            action = "log"
            msg = str(error)
        self.handled.append(action)
        return {"msg": msg, "action": action, "code": getattr(error, "code", 500)}

    def count(self):
        return len(self.handled)