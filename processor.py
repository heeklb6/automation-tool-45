import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class TransactionProcessor:
    """Processes and normalizes raw cryptocurrency exchange trade payloads."""

    def __init__(self, supported_symbols: List[str]):
        self.supported_symbols = [s.upper() for s in supported_symbols]

    def normalize_trade(self, raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extracts and formats trade metrics from raw exchange data."""
        try:
            symbol = str(raw_data.get("symbol", "")).upper()
            if symbol not in self.supported_symbols:
                logger.warning("Unsupported trading pair encountered: %s", symbol)
                return None

            price = float(raw_data.get("price", 0.0))
            amount = float(raw_data.get("amount", 0.0))
            side = str(raw_data.get("side", "")).lower()

            if price <= 0 or amount <= 0 or side not in ("buy", "sell"):
                logger.error("Invalid trade payload metrics: %s", raw_data)
                return None

            return {
                "symbol": symbol,
                "price": price,
                "amount": amount,
                "total": round(price * amount, 8),
                "side": side,
                "timestamp": raw_data.get("timestamp"),
            }
        except (ValueError, TypeError) as err:
            logger.error("Failed to normalize trade payload: %s", err)
            return None

    def batch_process(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters and normalizes a batch of trade records."""
        valid_trades = []
        for record in records:
            processed = self.normalize_trade(record)
            if processed:
                valid_trades.append(processed)
        return valid_trades