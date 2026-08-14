import requests

class CryptoAPI:
    BASE_URL = 'https://api.coingecko.com/api/v3/'

    def get_price(self, coin_id):
        url = f'{self.BASE_URL}simple/price?ids={coin_id}&vs_currencies=usd'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('API request failed')

    def get_market_data(self, coin_id):
        url = f'{self.BASE_URL}coins/{coin_id}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('API request failed')

if __name__ == '__main__':
    crypto_api = CryptoAPI()
    try:
        price = crypto_api.get_price('bitcoin')
        market_data = crypto_api.get_market_data('bitcoin')
        print('Bitcoin Price:', price)
        print('Market Data:', market_data)
    except Exception as e:
        print('Error:', e)