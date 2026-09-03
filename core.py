import asyncio
import time
from typing import Dict, List, Optional

class PriceCache:
    def __init__(self, ttl: float = 5.0):
        self.ttl = ttl
        self._data: Dict[str, tuple[float, float]] = {}

    def get(self, symbol: str) -> Optional[float]:
        if symbol in self._data:
            timestamp, price = self._data[symbol]
            if time.time() - timestamp < self.ttl:
                return price
        return None

    def set(self, symbol: str, price: float) -> None:
        self._data[symbol] = (time.time(), price)

class MarketDataProcessor:
    def __init__(self):
        self.cache = PriceCache()

    async def fetch_ticker_price(self, symbol: str) -> float:
        cached = self.cache.get(symbol)
        if cached is not None:
            return cached
        
        await asyncio.sleep(0.02)  # Simulate API call latency
        mock_price = 65000.0 if symbol == 'BTC' else 3500.0
        self.cache.set(symbol, mock_price)
        return mock_price

    async def fetch_multiple_prices(self, symbols: List[str]) -> Dict[str, float]:
        tasks = [self.fetch_ticker_price(sym) for sym in symbols]
        prices = await asyncio.gather(*tasks)
        return dict(zip(symbols, prices))