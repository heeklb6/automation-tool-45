import time
import requests
from requests.exceptions import RequestException

def retry_request(url, method='GET', retries=3, backoff_factor=0.3, **kwargs):
    """
    Makes a network request with retry logic.

    Args:
        url (str): The URL to send the request to.
        method (str): HTTP method (default is 'GET').
        retries (int): Number of retries before giving up.
        backoff_factor (float): Factor to apply for exponential backoff.
        **kwargs: Additional arguments to pass to the request.

    Returns:
        Response object from the requests library.
    """
    for attempt in range(retries):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            if attempt < retries - 1:
                wait = backoff_factor * (2 ** attempt)  # Exponential backoff
                time.sleep(wait)
                continue
            else:
                raise e  # Raise exception if all retries fail
