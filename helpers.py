import logging
from typing import Optional, Any
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

def safe_api_call(func, *args, **kwargs) -> Optional[Any]:
    """Executes crypto exchange API calls with robust error handling."""
    try:
        return func(*args, **kwargs)
    except RequestException as e:
        logger.error(f"Network connectivity issue: {e}")
    except ValueError as e:
        logger.error(f"Invalid JSON response or parsing error: {e}")
    except Exception as e:
        logger.critical(f"Unexpected error in {func.__name__}: {e}")
    return None

def validate_order_size(amount: float, min_size: float) -> bool:
    """Ensures order constraints are met before execution."""
    try:
        if amount <= 0:
            raise ValueError("Order amount must be positive")
        if amount < min_size:
            logger.warning(f"Amount {amount} below minimum {min_size}")
            return False
        return True
    except (TypeError, ValueError) as e:
        logger.error(f"Validation failed: {e}")
        return False

def format_price(price: float, precision: int = 8) -> float:
    """Normalizes crypto asset price based on ticker precision."""
    try:
        return float(format(price, f'.{precision}f'))
    except (ValueError, TypeError):
        logger.error("Invalid price format encountered")
        return 0.0