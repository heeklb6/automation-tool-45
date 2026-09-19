class AutomationError(Exception):
    """Base exception for automation-tool-45."""
    pass

class ConnectionTimeoutError(AutomationError):
    """Raised when network requests exceed threshold."""
    pass

class ExchangeApiError(AutomationError):
    """Raised when the crypto exchange returns an error code."""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

class ValidationError(AutomationError):
    """Raised when input parameters fail schema validation."""
    pass

class InsufficientBalanceError(AutomationError):
    """Raised during trade execution if funds are low."""
    pass

class RateLimitExceeded(AutomationError):
    """Raised when API request frequency limits are hit."""
    def __init__(self, retry_after=60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry in {retry_after}s")