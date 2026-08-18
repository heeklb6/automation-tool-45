import requests
import json
from exceptions import CustomError

class CryptoProcessor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.HTTPError as http_err:
            raise CustomError(f'HTTP error occurred: {http_err}')
        except requests.exceptions.ConnectionError:
            raise CustomError('Could not connect to the server')
        except requests.exceptions.Timeout:
            raise CustomError('Request timed out')
        except requests.exceptions.RequestException as err:
            raise CustomError(f'An error occurred: {err}')
        return response.json()

    def process_data(self, data):
        if not isinstance(data, dict):
            raise CustomError('Invalid data format, expected dict')
        # Processing logic goes here...
        return data  # Assuming processing returns modified data

# Usage example
if __name__ == '__main__':
    processor = CryptoProcessor('https://api.coingecko.com/api/v3/coins/markets')
    try:
        data = processor.fetch_data()
        processed_data = processor.process_data(data)
        print(json.dumps(processed_data, indent=2))
    except CustomError as e:
        print(f'Error: {e}')