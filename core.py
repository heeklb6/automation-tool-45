import time
import requests

class CryptoDataFetcher:
    def __init__(self, api_url):
        self.api_url = api_url
        self.cache = {}  # To store API results
        self.cache_time = 300  # Cache expiration time in seconds
        self.last_fetched_time = 0

    def get_data(self, crypto_symbol):
        current_time = time.time()
        # Return cached data if it's still valid
        if crypto_symbol in self.cache and (current_time - self.last_fetched_time) < self.cache_time:
            return self.cache[crypto_symbol]
        # Fetch new data from the API if cache is expired or not available
        response = requests.get(f'{self.api_url}/{crypto_symbol}')
        if response.status_code == 200:
            self.cache[crypto_symbol] = response.json()
            self.last_fetched_time = current_time
            return self.cache[crypto_symbol]
        else:
            response.raise_for_status()

# Example usage
if __name__ == '__main__':
    fetcher = CryptoDataFetcher('https://api.coingecko.com/api/v3/simple/price')
    print(fetcher.get_data('bitcoin'))
    time.sleep(10)  # Simulate delay
    print(fetcher.get_data('bitcoin'))  # Should return cached data