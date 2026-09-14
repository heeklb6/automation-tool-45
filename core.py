import functools
import time
from typing import Callable, Any

# Cache for crypto price calculations to reduce API overhead
_price_cache = {}
_cache_ttl = 60

def memoize_crypto_data(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        now = time.time()
        if key in _price_cache:
            val, timestamp = _price_cache[key]
            if now - timestamp < _cache_ttl:
                return val
        
        result = func(*args, **kwargs)
        _price_cache[key] = (result, now)
        return result
    return wrapper

class CryptoProcessor:
    def __init__(self, asset_pair: str):
        self.asset_pair = asset_pair

    @memoize_crypto_data
    def fetch_market_depth(self, depth: int = 10) -> dict:
        # Simulated heavy network-bound operation
        time.sleep(0.5)
        return {"pair": self.asset_pair, "depth": depth, "status": "live"}

    def batch_process(self, requests: list) -> list:
        # Optimization: process in chunks to minimize latency
        return [self.fetch_market_depth(r) for r in requests]

if __name__ == '__main__':
    proc = CryptoProcessor('BTC-USD')
    # Repeated calls return cached data instantly
    print(proc.fetch_market_depth(10))
    print(proc.fetch_market_depth(10))