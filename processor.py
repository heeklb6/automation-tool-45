import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles normalization and validation of incoming crypto trade data."""

    def __init__(self, exchange: str):
        self.exchange = exchange

    def process_payload(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filters out invalid trades and normalizes numeric values."""
        cleaned_data = []
        for entry in data:
            try:
                if not entry.get('price') or not entry.get('amount'):
                    continue
                
                normalized = {
                    'pair': entry['pair'].upper(),
                    'price': float(entry['price']),
                    'amount': float(entry['amount']),
                    'timestamp': entry.get('timestamp')
                }
                cleaned_data.append(normalized)
            except (ValueError, KeyError, TypeError) as e:
                logger.warning(f"Skipping invalid trade entry: {e}")
                continue
        return cleaned_data

    def batch_process(self, datasets: List[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Aggregates multiple trade batches into a single cleaned list."""
        results = []
        for batch in datasets:
            results.extend(self.process_payload(batch))
        return results