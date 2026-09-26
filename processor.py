"""Crypto trade payload processor module for order execution."""

from typing import Dict, List, Any
from decimal import Decimal


class TradeProcessor:
    """Processes raw market data and formats orders for execution."""

    def __init__(self, fee_rate: float = 0.001) -> None:
        """Initialize processor with default trading fee rate."""
        self.fee_rate: Decimal = Decimal(str(fee_rate))

    def calculate_net_amount(self, amount: float, price: float) -> Decimal:
        """Calculate net trade cost including configured exchange fees.

        Args:
            amount: Quantity of cryptocurrency being traded.
            price: Unit execution price in quote currency.

        Returns:
            Total gross cost plus exchange fee as Decimal.
        """
        qty = Decimal(str(amount))
        unit_price = Decimal(str(price))
        gross = qty * unit_price
        fee = gross * self.fee_rate
        return gross + fee

    def filter_valid_trades(
        self, trades: List[Dict[str, Any]], min_volume: float
    ) -> List[Dict[str, Any]]:
        """Filter trade payloads that meet minimum volume criteria.

        Args:
            trades: List of raw trade data dictionaries from ticker stream.
            min_volume: Minimum threshold volume in quote currency.

        Returns:
            Filtered list of structured trade event objects.
        """
        valid_trades: List[Dict[str, Any]] = []
        min_vol_dec = Decimal(str(min_volume))

        for trade in trades:
            price = Decimal(str(trade.get("price", 0)))
            size = Decimal(str(trade.get("size", 0)))
            volume = price * size

            if volume >= min_vol_dec:
                valid_trades.append({
                    "symbol": str(trade.get("symbol", "")),
                    "volume": float(volume),
                    "side": str(trade.get("side", "buy")).upper(),
                })

        return valid_trades
