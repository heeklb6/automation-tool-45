import logging
from typing import Dict, Any, Callable

logger = logging.getLogger("automation_tool.handler")

class CryptoEventHandler:
    """Dispatches and processes incoming blockchain and market events."""

    def __init__(self) -> None:
        self._registry: Dict[str, Callable[[Dict[str, Any]], None]] = {}
        self._setup_default_handlers()

    def register_handler(self, event_type: str, handler: Callable[[Dict[str, Any]], None]) -> None:
        """Registers a custom callback for a specific event type."""
        self._registry[event_type] = handler

    def _setup_default_handlers(self) -> None:
        self.register_handler("price_alert", self._process_price_alert)
        self.register_handler("transaction", self._process_transaction)

    def handle_event(self, event: Dict[str, Any]) -> bool:
        """Validates and routes incoming crypto events to registered handlers."""
        event_type = event.get("type")
        if not event_type:
            logger.warning("Received event without a valid type")
            return False

        handler = self._registry.get(event_type)
        if not handler:
            logger.warning(f"No handler registered for event type: {event_type}")
            return False

        try:
            data = event.get("data", {})
            handler(data)
            return True
        except Exception as e:
            logger.error(f"Error executing handler for {event_type}: {e}")
            return False

    def _process_price_alert(self, data: Dict[str, Any]) -> None:
        symbol = data.get("symbol", "UNKNOWN")
        price = data.get("price", 0.0)
        logger.info(f"Price alert triggered: {symbol} at {price}")

    def _process_transaction(self, data: Dict[str, Any]) -> None:
        tx_hash = data.get("tx_hash", "0x")
        amount = data.get("amount", 0.0)
        logger.info(f"Transaction detected: {tx_hash} with amount {amount}")