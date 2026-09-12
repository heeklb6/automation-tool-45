import logging
import re
from typing import Dict, Any, List

# Setup logger
logger = logging.getLogger("automation-tool-45.processor")

# Hex address validation for EVM compatible chains
ADDRESS_REGEX = re.compile(r"^0x[a-fA-F0-9]{40}$")
SUPPORTED_ASSETS = {"BTC", "ETH", "USDT", "USDC"}

class TransactionProcessor:
    def __init__(self):
        self.processed_count = 0
        self.failed_count = 0

    def validate_transaction(self, tx: Dict[str, Any]) -> bool:
        """Validates structure and fields of a crypto transaction."""
        required_keys = {"tx_id", "sender", "recipient", "amount", "asset"}
        if not required_keys.issubset(tx.keys()):
            logger.error(f"Missing required fields in transaction: {tx.get('tx_id', 'unknown')}")
            return False

        if not isinstance(tx["sender"], str) or not ADDRESS_REGEX.match(tx["sender"]):
            logger.error(f"Invalid sender address format for tx {tx.get('tx_id')}")
            return False

        if not isinstance(tx["recipient"], str) or not ADDRESS_REGEX.match(tx["recipient"]):
            logger.error(f"Invalid recipient address format for tx {tx.get('tx_id')}")
            return False

        if not isinstance(tx["amount"], (int, float)) or tx["amount"] <= 0:
            logger.error(f"Invalid transaction amount: {tx.get('amount')} for tx {tx.get('tx_id')}")
            return False

        if tx["asset"] not in SUPPORTED_ASSETS:
            logger.error(f"Unsupported asset: {tx.get('asset')} for tx {tx.get('tx_id')}")
            return False

        return True

    def process_transactions(self, transactions: List[Dict[str, Any]]) -> Dict[str, int]:
        """Main processing loop that validates and executes transactions."""
        logger.info(f"Starting processing of {len(transactions)} transactions")
        
        for tx in transactions:
            try:
                if not self.validate_transaction(tx):
                    self.failed_count += 1
                    continue
                
                # Simulate successful execution of the crypto transaction
                logger.info(f"Transaction {tx['tx_id']} successfully validated and processed")
                self.processed_count += 1
            except Exception as e:
                logger.error(f"Unexpected error processing tx {tx.get('tx_id', 'unknown')}: {e}")
                self.failed_count += 1

        return {"processed": self.processed_count, "failed": self.failed_count}