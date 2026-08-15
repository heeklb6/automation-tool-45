API_BASE_URL = 'https://api.crypto.com'
DEFAULT_TIMEOUT = 30
SUPPORTED_CURRENCIES = ['BTC', 'ETH', 'LTC', 'XRP']
ERROR_MESSAGES = {
    'network_error': 'Network error, please try again.',
    'invalid_currency': 'The specified currency is not supported.',
    'rate_limit': 'Rate limit exceeded, please wait before retrying.'
}
CURRENCY_SYMBOLS = {
    'BTC': '₿',
    'ETH': 'Ξ',
    'LTC': 'Ł',
    'XRP': 'X'
}
MARKET_STATUS = {
    'bull': 'Bull market',
    'bear': 'Bear market',
    'sideways': 'Sideways market'
}
