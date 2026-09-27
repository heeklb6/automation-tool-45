"""Market data and transaction payload processor for crypto trading pipeline."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional


@dataclass
class TradeSignal:
    symbol: str
    action: str
    price: float
    quantity: float
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class OrderProcessor:
    """Processes raw exchange payloads into normalized trading signals."""

    def __init__(self, min_order_value: float = 10.0):
        self.min_order_value = min_order_value
        self.processed_count = 0

    def parse_payload(self, raw_data: Dict) -> Optional[TradeSignal]:
        """Validates and parses raw websocket or REST trade payload."""
        symbol = raw_data.get("symbol")
        side = raw_data.get("side", "").upper()
        price = float(raw_data.get("price", 0.0))
        qty = float(raw_data.get("quantity", 0.0))

        if not symbol or side not in ("BUY", "SELL"):
            return None

        total_value = price * qty
        if total_value < self.min_order_value:
            return None

        return TradeSignal(
            symbol=symbol,
            action=side,
            price=price,
            quantity=qty,
        )

    def process_batch(self, payloads: List[Dict]) -> List[TradeSignal]:
        """Filters and reorganizes a list of incoming market payloads."""
        signals = []
        for payload in payloads:
            signal = self.parse_payload(payload)
            if signal:
                signals.append(signal)
                self.processed_count += 1
        return signals