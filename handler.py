import logging
from typing import Dict, Any
from core import CryptoEngine

logger = logging.getLogger(__name__)

class TransactionHandler:
    """Handles execution flow for automated crypto trades."""

    def __init__(self, engine: CryptoEngine):
        self.engine = engine

    def process_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validates and executes trade requests."""
        if not self._is_valid(data):
            return {"status": "error", "message": "invalid payload"}

        try:
            result = self.engine.execute(data)
            return {"status": "success", "tx_id": result}
        except Exception as e:
            logger.error(f"Execution failure: {e}")
            return {"status": "error", "message": str(e)}

    def _is_valid(self, data: Dict[str, Any]) -> bool:
        """Basic structure validation for incoming orders."""
        required = ['asset', 'amount', 'side']
        return all(key in data for key in required)