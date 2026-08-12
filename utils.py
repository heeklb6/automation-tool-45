import time
import random
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, backoff_factor=1):
    """Attempt to perform a network request with retry logic.
    
    Args:
        url (str): The URL to request.
        max_retries (int): The maximum number of retry attempts.
        backoff_factor (int): The multiplier for backoff time.
    
    Returns:
        Response object if the request was successful; raises exception otherwise.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise RuntimeError(f'Failed to fetch {url} after {attempts} attempts')
            wait_time = backoff_factor * (2 ** (attempts - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)
            print(f'Retrying {url} (Attempt {attempts}/{max_retries})...')