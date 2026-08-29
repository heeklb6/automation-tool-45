import time
import random

class Processor:
    def __init__(self, max_retries=3, base_delay=1):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute_with_retry(self, func, *args, **kwargs):
        # Retry logic for network operations in crypto automation
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_error = e
                if attempt == self.max_retries:
                    break
                delay = self.base_delay * (2 ** (attempt - 1))
                delay += random.uniform(0, 0.5)  # jitter
                time.sleep(delay)
        raise last_error

    def fetch_price(self, symbol):
        # Simulate network call to crypto exchange API
        def network_call():
            # Replace with actual requests.get in production
            if random.random() < 0.4:
                raise ConnectionError("Simulated network failure")
            # Mock response for crypto price
            mock_prices = {
                "BTC": 65000.50,
                "ETH": 2600.75,
                "SOL": 150.25
            }
            return mock_prices.get(symbol, 0.0)

        return self.execute_with_retry(network_call)

    def broadcast_transaction(self, tx_data):
        # Retry sending transaction to blockchain node
        def network_call():
            if random.random() < 0.25:
                raise TimeoutError("Network timeout during broadcast")
            return "Transaction broadcast successful: " + tx_data[:10] + "..."

        return self.execute_with_retry(network_call)

# Usage example
if __name__ == "__main__":
    proc = Processor(max_retries=4, base_delay=0.5)
    try:
        price = proc.fetch_price("BTC")
        print(f"Price: {price}")
        tx = proc.broadcast_transaction("0xabc123def456")
        print(tx)
    except Exception as e:
        print(f"Operation failed: {e}")