import time
import logging
from functools import wraps
from requests.exceptions import RequestException

logger = logging.getLogger("automation-tool-45")

def retry_network_operation(max_retries=3, delay=2, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except RequestException as e:
                    logger.warning(f"Network error on attempt {attempt}/{max_retries}: {e}")
                    if attempt == max_retries:
                        logger.error("Max retries reached. Operation failed.")
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=1)
def fetch_crypto_ticker(session, url):
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
