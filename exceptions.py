class AutomationError(Exception):
    """Base exception for automation-tool-45."""
    pass

class NetworkTimeoutError(AutomationError):
    """Raised when external crypto exchange APIs timeout."""
    pass

class InsufficientFundsError(AutomationError):
    """Raised when account balance is too low for trade."""
    pass

class RateLimitExceededError(AutomationError):
    """Raised when API request frequency limits are hit."""
    pass

class ConfigurationError(AutomationError):
    """Raised for invalid environment or config settings."""
    pass

def handle_exception(e: Exception) -> str:
    """Format exception message for logging system."""
    if isinstance(e, AutomationError):
        return f"[AUTOMATION_ERROR] {type(e).__name__}: {str(e)}"
    return f"[UNHANDLED_ERROR] {type(e).__name__}: {str(e)}"

if __name__ == "__main__":
    try:
        raise InsufficientFundsError("Wallet balance below order threshold")
    except AutomationError as err:
        print(handle_exception(err))