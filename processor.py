import json
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger("automation_tool.processor")

class CryptoDataProcessor:
    """Processes market data with robust handling of edge cases and anomalies."""

    def __init__(self, decimal_places: int = 8):
        self.decimal_places = decimal_places

    def parse_ticker_payload(self, raw_payload: str) -> Optional[Dict[str, Any]]:
        """Parses raw JSON data, sanitizing bad types and handling empty inputs."""
        if not raw_payload or not raw_payload.strip():
            logger.warning("Empty payload received")
            return None

        try:
            data = json.loads(raw_payload)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {e}")
            return None

        if not isinstance(data, dict):
            logger.error(f"Expected dict but got {type(data).__name__}")
            return None

        # Extract and safely convert values to avoid ValueErrors
        try:
            symbol = str(data.get("symbol", "")).strip().upper()
            if not symbol:
                logger.warning("Missing or empty symbol in payload")
                return None

            price = float(data.get("lastPrice") or data.get("price") or 0)
            volume = float(data.get("volume") or 0)

            if price <= 0:
                logger.warning(f"Non-positive price encountered for {symbol}: {price}")
                return None

            return {
                "symbol": symbol,
                "price": round(price, self.decimal_places),
                "volume": round(volume, self.decimal_places)
            }
        except (ValueError, TypeError) as e:
            logger.error(f"Data type conversion error in ticker payload: {e}")
            return None

    def safe_calculate_vwap(self, aggregate_data: List[Dict[str, float]]) -> float:
        """Calculates Volume Weighted Average Price while mitigating division by zero."""
        total_value = 0.0
        total_volume = 0.0

        for entry in aggregate_data:
            try:
                price = float(entry.get("price", 0))
                volume = float(entry.get("volume", 0))
                if price < 0 or volume < 0:
                    continue  # skip outlier anomalies
                total_value += price * volume
                total_volume += volume
            except (ValueError, TypeError):
                continue

        if total_volume <= 0.0:
            logger.warning("Cumulative volume is zero or negative; VWAP cannot be calculated")
            return 0.0

        return round(total_value / total_volume, self.decimal_places)