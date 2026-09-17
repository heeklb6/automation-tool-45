class AutomationError(Exception):
    """Base exception for automation-tool-45."""
    pass

class ExchangeConnectionError(AutomationError):
    """Raised when exchange connectivity fails."""
    pass

class InsufficientFundsError(AutomationError):
    """Raised when wallet balance is too low."""
    pass

class OrderPlacementError(AutomationError):
    """Raised when an order fails to execute."""
    pass

class RateLimitExceededError(AutomationError):
    """Raised when API rate limits are hit."""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded, retry after {retry_after}s")

class ConfigValidationError(AutomationError):
    """Raised when configuration values are invalid."""
    pass

def raise_if_failed(response: dict):
    """Helper to validate API responses for errors."""
    if response.get("status") == "error":
        error_code = response.get("code")
        message = response.get("message", "Unknown error")
        
        if error_code == "INSUFFICIENT_FUNDS":
            raise InsufficientFundsError(message)
        elif error_code == "RATE_LIMIT":
            raise RateLimitExceededError()
        else:
            raise AutomationError(message)