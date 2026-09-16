import re
from typing import List, Dict, Any, Tuple

# Regular expressions for validating common crypto primitives
TX_HASH_REGEX = re.compile(r"^0x[a-fA-F0-9]{64}$")
ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
SUPPORTED_SYMBOLS = {"BTC", "ETH", "USDT", "USDC", "SOL"}

class TransactionProcessor:
    """Processes and validates cryptocurrency transaction payloads before ingestion."""

    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0

    def validate_payload(self, data: Dict[str, Any]) -> Tuple[bool, str]:
        """Performs schema and semantic validation on incoming transaction data."""
        required_keys = {"tx_hash", "recipient", "amount", "symbol"}
        if not required_keys.issubset(data.keys()):
            missing = required_keys - data.keys()
            return False, f"Missing required fields: {', '.join(missing)}"

        if not TX_HASH_REGEX.match(str(data["tx_hash"])):
            return False, "Invalid transaction hash format"

        if not ADDRESS_REGEX.match(str(data["recipient"])):
            return False, "Invalid recipient address format"

        try:
            amount = float(data["amount"])
            if amount <= 0:
                return False, "Transaction amount must be strictly positive"
        except (ValueError, TypeError):
            return False, "Numeric amount is invalid or unparseable"

        if str(data["symbol"]).upper() not in SUPPORTED_SYMBOLS:
            return False, f"Unsupported ticker symbol: {data['symbol']}"

        return True, "Valid"

    def process_batch(self, batch: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Executes validation checks in the loop and prepares logs."""
        results = []
        for index, raw_item in enumerate(batch):
            is_valid, reason = self.validate_payload(raw_item)
            if not is_valid:
                self.failed_count += 1
                results.append({
                    "index": index,
                    "status": "rejected",
                    "error": reason
                })
                continue

            self.processed_count += 1
            results.append({
                "index": index,
                "status": "approved",
                "tx_hash": raw_item["tx_hash"],
                "formatted_amount": f"{float(raw_item['amount']):.6f} {raw_item['symbol'].upper()}"
            })

        return {
            "batch_total": len(batch),
            "successful": self.processed_count,
            "failed": self.failed_count,
            "details": results
        }