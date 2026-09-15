import logging
from typing import Dict, Any
from core import CryptoEngine

logger = logging.getLogger(__name__)

class TradeHandler:
    def __init__(self, engine: CryptoEngine):
        self.engine = engine
        self.active_tasks = {}

    def handle_signal(self, payload: Dict[str, Any]) -> bool:
        """Process incoming trading signals from webhook."""
        symbol = payload.get("symbol")
        side = payload.get("side")
        
        if not symbol or side not in ["buy", "sell"]:
            logger.error(f"invalid signal structure: {payload}")
            return False

        try:
            order_id = self.engine.execute(symbol, side, payload.get("amount", 0))
            self.active_tasks[order_id] = payload
            logger.info(f"order {order_id} processed for {symbol}")
            return True
        except Exception as e:
            logger.exception(f"execution failure for {symbol}: {e}")
            return False

    def cleanup_stale_orders(self):
        """Prune local cache of completed operations."""
        keys_to_remove = [k for k, v in self.active_tasks.items() if v.get("status") == "closed"]
        for k in keys_to_remove:
            del self.active_tasks[k]
        logger.debug(f"cleanup completed, {len(keys_to_remove)} tasks removed")