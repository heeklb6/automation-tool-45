"""Crypto transaction and market data processing module."""

from decimal import Decimal
from typing import Any, Dict, List, Optional


class TradeProcessor:
    """Processes raw trade data and formats order payloads for exchange execution."""

    def __init__(self, default_fee_rate: Decimal = Decimal("0.001")) -> None:
        self.default_fee_rate = default_fee_rate

    def calculate_net_amount(
        self, price: Decimal, quantity: Decimal, is_buy: bool
    ) -> Decimal:
        """Calculate total trade amount including network fees.

        Args:
            price: Asset execution price.
            quantity: Trade order size.
            is_buy: True if buy order, False if sell.

        Returns:
            Net value of trade after fee deduction.
        """
        gross_value = price * quantity
        fee = gross_value * self.default_fee_rate
        return gross_value + fee if is_buy else gross_value - fee

    def parse_ticker_data(
        self, raw_data: Dict[str, Any]
    ) -> Dict[str, Optional[Decimal]]:
        """Normalize exchange ticker payload into a structured dictionary.

        Args:
            raw_data: Unstructured ticker JSON response.

        Returns:
            Normalized dictionary containing bid, ask, and last prices.
        """
        parsed: Dict[str, Optional[Decimal]] = {}
        for key in ("bid", "ask", "last"):
            val = raw_data.get(key)
            parsed[key] = Decimal(str(val)) if val is not None else None
        return parsed

    def filter_high_volume_pairs(
        self, pairs: List[Dict[str, Any]], min_volume_usd: Decimal
    ) -> List[str]:
        """Filter trading pairs that meet minimum 24h volume criteria.

        Args:
            pairs: List of trading pair market details.
            min_volume_usd: Threshold 24-hour USD volume.

        Returns:
            List of symbol names meeting the volume threshold.
        """
        valid_symbols: List[str] = []
        for pair in pairs:
            volume = Decimal(str(pair.get("volume_24h", 0)))
            if volume >= min_volume_usd and "symbol" in pair:
                valid_symbols.append(str(pair["symbol"]))
        return valid_symbols