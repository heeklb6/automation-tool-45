class CryptoAutomationError(Exception):
    """Base exception for all automation-tool-45 errors."""
    pass

class ExchangeConnectionError(CryptoAutomationError):
    """Raised when communication with exchange API fails."""
    pass

class RateLimitExceeded(CryptoAutomationError):
    """Raised when API request limits are reached."""
    pass

class InsufficientFundsError(CryptoAutomationError):
    """Raised when wallet balance is below transaction minimum."""
    pass

class OrderPlacementError(CryptoAutomationError):
    """Raised when order execution fails on exchange."""
    pass

class ConfigurationError(CryptoAutomationError):
    """Raised for missing or invalid config keys."""
    pass

def handle_exception(e: Exception) -> str:
    """Returns standardized error message based on exception type."""
    if isinstance(e, RateLimitExceeded):
        return "Critical: exchange rate limit hit. Pausing execution."
    elif isinstance(e, InsufficientFundsError):
        return "Failure: insufficient assets for requested trade."
    return f"Unexpected system error: {str(e)}"