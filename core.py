from typing import List, Dict, Optional

class CryptoProcessor:
    """Handles execution of automated trading tasks."""

    def __init__(self, exchange_id: str, rate_limit: float = 0.5):
        self.exchange_id: str = exchange_id
        self.rate_limit: float = rate_limit
        self.active_orders: List[Dict[str, float]] = []

    def add_order(self, pair: str, amount: float, price: float) -> bool:
        """Adds a new order to the internal queue."""
        if amount <= 0 or price <= 0:
            return False
        
        order = {"pair": pair, "amount": amount, "price": price}
        self.active_orders.append(order)
        return True

    def get_market_summary(self) -> Dict[str, Optional[float]]:
        """Returns simplified market statistics for tracked pairs."""
        if not self.active_orders:
            return {"avg_price": 0.0, "total_volume": 0.0}
            
        total_val = sum(o["price"] * o["amount"] for o in self.active_orders)
        total_vol = sum(o["amount"] for o in self.active_orders)
        
        return {
            "avg_price": total_val / total_vol if total_vol > 0 else 0.0,
            "total_volume": total_vol
        }

    def clear_orders(self) -> None:
        """Resets the current order list."""
        self.active_orders.clear()