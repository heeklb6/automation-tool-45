import asyncio
from functools import lru_cache
from typing import Dict, List, Tuple


class MarketDataEngine:
    """Core engine optimized for high-throughput crypto market data processing."""

    def __init__(self, cache_size: int = 2048):
        self.cache_size = cache_size
        self._ticker_cache: Dict[str, Tuple[float, float]] = {}
        self._queue: asyncio.Queue = asyncio.Queue()

    @lru_cache(maxsize=2048)
    def calculate_vwap(self, prices: Tuple[float, ...], volumes: Tuple[float, ...]) -> float:
        """Calculate Volume-Weighted Average Price with cached execution."""
        if not prices or len(prices) != len(volumes):
            return 0.0

        total_volume = sum(volumes)
        if total_volume == 0.0:
            return 0.0

        weighted_sum = sum(p * v for p, v in zip(prices, volumes))
        return round(weighted_sum / total_volume, 8)

    async def batch_process_updates(self, updates: List[Dict[str, float]]) -> Dict[str, float]:
        """Process bulk price updates in vectorized dictionary batches for speed."""
        aggregated: Dict[str, List[float]] = {}

        for update in updates:
            symbol = update.get("symbol")
            price = update.get("price")
            if symbol and price is not None:
                if symbol not in aggregated:
                    aggregated[symbol] = []
                aggregated[symbol].append(price)

        return {
            symbol: round(sum(prices) / len(prices), 8)
            for symbol, prices in aggregated.items()
            if prices
        }

    def purge_cache(self) -> None:
        """Clear LRU cache to prevent stale pricing data accumulation."""
        self.calculate_vwap.cache_clear()
        self._ticker_cache.clear()
