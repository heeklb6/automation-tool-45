import bisect
from typing import List, Tuple

class OrderBook:
    """Optimized order book tracker with O(log N) lookup and update operations."""
    def __init__(self) -> None:
        # Bid prices stored negated to facilitate descending order sorting with bisect
        self.bid_prices: List[float] = []
        self.bid_qtys: List[float] = []
        # Ask prices stored normally (ascending order)
        self.ask_prices: List[float] = []
        self.ask_qtys: List[float] = []

    def update_bid(self, price: float, quantity: float) -> None:
        """Update or insert bid price level with optimized binary search insertion."""
        neg_price = -price
        idx = bisect.bisect_left(self.bid_prices, neg_price)
        
        if idx < len(self.bid_prices) and self.bid_prices[idx] == neg_price:
            if quantity <= 0.0:
                self.bid_prices.pop(idx)
                self.bid_qtys.pop(idx)
            else:
                self.bid_qtys[idx] = quantity
        elif quantity > 0.0:
            self.bid_prices.insert(idx, neg_price)
            self.bid_qtys.insert(idx, quantity)

    def update_ask(self, price: float, quantity: float) -> None:
        """Update or insert ask price level with optimized binary search insertion."""
        idx = bisect.bisect_left(self.ask_prices, price)
        
        if idx < len(self.ask_prices) and self.ask_prices[idx] == price:
            if quantity <= 0.0:
                self.ask_prices.pop(idx)
                self.ask_qtys.pop(idx)
            else:
                self.ask_qtys[idx] = quantity
        elif quantity > 0.0:
            self.ask_prices.insert(idx, price)
            self.ask_qtys.insert(idx, quantity)

    def get_depth(self, depth: int) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        """Retrieve top N depth levels for bids and asks."""
        bids = [(-self.bid_prices[i], self.bid_qtys[i]) for i in range(min(depth, len(self.bid_prices)))]
        asks = [(self.ask_prices[i], self.ask_qtys[i]) for i in range(min(depth, len(self.ask_prices)))]
        return bids, asks

    def get_mid_price(self) -> float:
        """Retrieve current market mid price."""
        if not self.bid_prices or not self.ask_prices:
            return 0.0
        return (-self.bid_prices[0] + self.ask_prices[0]) / 2.0