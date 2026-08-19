import json
import requests
from datetime import datetime

class CryptoDataError(Exception):
    pass

def fetch_crypto_price(symbol: str) -> dict:
    try:
        url = f'https://api.coindesk.com/v1/bpi/currentprice/{symbol}.json'
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return {
            'symbol': symbol,
            'price': data['bpi'][symbol]['rate_float'],
            'currency': data['bpi'][symbol]['code'],
            'time': datetime.utcfromtimestamp(data['time']['updatedISO']).isoformat(),
        }
    except requests.exceptions.RequestException as e:
        raise CryptoDataError(f'Failed to fetch price data: {e}') from e
    except (KeyError, TypeError) as e:
        raise CryptoDataError('Error parsing crypto price data') from e

# Example usage (commented out)
# price_info = fetch_crypto_price('USD')
# print(price_info)  
