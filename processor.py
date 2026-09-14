from typing import List, Dict, Any, Optional

class CryptoProcessor:
    """Handles trade execution and portfolio data aggregation."""

    def __init__(self, api_key: str, threshold: float = 0.05) -> None:
        self.api_key: str = api_key
        self.threshold: float = threshold
        self.active_assets: List[str] = []

    def validate_price(self, price: float) -> bool:
        """Checks if price is positive and within operating bounds."""
        return price > 0

    def calculate_position(self, balance: float, current_price: float) -> Optional[float]:
        """Determines trade size based on available balance and price."""
        if not self.validate_price(current_price):
            return None
        return balance * self.threshold / current_price

    def update_portfolio(self, data: Dict[str, Any]) -> None:
        """Updates internal asset list from incoming dictionary stream."""
        new_assets: List[str] = data.get("symbols", [])
        self.active_assets = list(set(self.active_assets + new_assets))

    def get_summary(self) -> Dict[str, Any]:
        """Returns status of the processor instance."""
        return {
            "threshold": self.threshold,
            "assets_tracked": len(self.active_assets)
        }