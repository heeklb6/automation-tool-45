import logging
import re
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
SUPPORTED_SYMBOLS = {"BTC", "ETH", "USDT", "USDC", "SOL"}


def validate_transaction_input(payload: Dict[str, Any]) -> bool:
    """Validate incoming crypto transaction payload before execution."""
    if not isinstance(payload, dict):
        logging.warning("Invalid payload format: expected dict")
        return False

    address = payload.get("recipient")
    amount = payload.get("amount")
    symbol = payload.get("symbol")

    if not address or not isinstance(address, str) or not ETH_ADDRESS_PATTERN.match(address):
        logging.warning(f"Invalid recipient address: {address}")
        return False

    if not isinstance(amount, (int, float)) or amount <= 0:
        logging.warning(f"Invalid transaction amount: {amount}")
        return False

    if not symbol or not isinstance(symbol, str) or symbol.upper() not in SUPPORTED_SYMBOLS:
        logging.warning(f"Unsupported crypto symbol: {symbol}")
        return False

    return True


def process_transaction_queue(queue: List[Dict[str, Any]]) -> Dict[str, int]:
    """Process batch of transactions with input validation in main loop."""
    stats = {"processed": 0, "skipped": 0}

    for idx, item in enumerate(queue):
        logging.info(f"Processing item #{idx + 1}")
        
        if not validate_transaction_input(item):
            logging.error(f"Skipping invalid item #{idx + 1}")
            stats["skipped"] += 1
            continue

        symbol = item["symbol"].upper()
        logging.info(f"Successfully dispatched {item['amount']} {symbol} to {item['recipient']}")
        stats["processed"] += 1

    return stats