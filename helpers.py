import requests
import json

def fetch_data(url: str) -> dict:
    """Fetch data from the provided URL and return as a dictionary."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Convert JSON response to dictionary
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return {}
    except requests.exceptions.RequestException as err:
        print(f"Network error occurred: {err}")
        return {}


def parse_cryptocurrency_data(data: dict) -> list:
    """Parse cryptocurrency data and return structured data as a list of dictionaries."""
    parsed_data = []
    for item in data.get('cryptocurrencies', []):
        parsed_data.append({
            'name': item.get('name'),
            'symbol': item.get('symbol'),
            'market_cap': item.get('market_cap'),
            'price': item.get('price')
        })
    return parsed_data


def save_to_file(data: dict, filename: str) -> None:
    """Save the given data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

