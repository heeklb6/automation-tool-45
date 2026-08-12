API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

BASE_URL = "https://api.cryptoexchange.com"

# Timeout settings
REQUEST_TIMEOUT = 10  # in seconds

# Define possible order types
ORDER_TYPES = ["buy", "sell", "limit", "market"]

# Define supported currencies
SUPPORTED_CURRENCIES = ["BTC", "ETH", "LTC", "XRP"]

# Fee structures
TRANSACTION_FEE_PERCENT = 0.1
WITHDRAWAL_FEE = {"BTC": 0.0005, "ETH": 0.01, "LTC": 0.001, "XRP": 0.01}

# Logging constants
LOG_LEVEL = "INFO"
MAX_LOG_SIZE = 10485760  # 10 MB
MAX_LOG_FILES = 5

# Environment settings
ENVIRONMENT = "production"  # Change to 'development' for testing
