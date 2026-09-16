class CryptoBaseException(Exception):
    """Base exception for automation-tool-45 operations."""
    pass

class ExchangeConnectionError(CryptoBaseException):
    """Raised when the crypto exchange API is unreachable."""
    pass

class InsufficientFundsError(CryptoBaseException):
    """Raised when account balance is too low for trades."""
    pass

class RateLimitExceeded(CryptoBaseException):
    """Raised when API requests exceed threshold."""
    def __init__(self, retry_after: int = 60):
        self.retry_after = retry_after
        super().__init__(f"Rate limit hit. Wait {retry_after}s.")

class ValidationError(CryptoBaseException):
    """Raised when payload data is malformed."""
    pass

class OrderExecutionError(CryptoBaseException):
    """Raised when a trade fails at the exchange."""
    pass