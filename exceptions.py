class CryptoAutomationError(Exception):
    """Base exception for automation-tool-45."""
    pass

class ExchangeConnectionError(CryptoAutomationError):
    """Raised when the exchange API is unreachable."""
    pass

class InsufficientBalanceError(CryptoAutomationError):
    """Raised when order execution exceeds wallet funds."""
    pass

class OrderPlacementError(CryptoAutomationError):
    """Raised when an order request is rejected by exchange."""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

class DataValidationError(CryptoAutomationError):
    """Raised when incoming market data is malformed."""
    pass

def handle_crypto_exception(e: Exception) -> str:
    """Helper to format exception messages for logging."""
    if isinstance(e, CryptoAutomationError):
        return f"[CRITICAL] {type(e).__name__}: {str(e)}"
    return f"[UNKNOWN_ERROR] {str(e)}"