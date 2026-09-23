import time
import functools
import logging

# crypto network operations retry decorator
def retry_network_op(retries=3, delay=2, backoff=2):
    """Retry a function with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logging.error(f"Final attempt {attempt + 1} failed: {e}")
                        raise
                    
                    logging.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

# common status codes for exchange api calls
EXCHANGE_RATE_LIMIT = 429
EXCHANGE_MAINTENANCE = 503

@retry_network_op(retries=5, delay=1)
def fetch_price_data(ticker: str):
    """Example usage for external crypto price fetch."""
    # implementation logic for network call
    return True