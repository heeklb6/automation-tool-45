import time
import hashlib
import json
from typing import Dict, Any, List

def hash_seed(seed: str) -> str:
    """Create hash from seed for deterministic wallet generation."""
    return hashlib.sha256(seed.encode('utf-8')).hexdigest()

def validate_address(address: str) -> bool:
    """Validate ethereum style address."""
    if not address or not address.startswith('0x'):
        return False
    if len(address) != 42:
        return False
    try:
        int(address[2:], 16)
        return True
    except ValueError:
        return False

def to_wei(amount: float, decimals: int = 18) -> int:
    """Convert decimal amount to wei."""
    return int(amount * (10 ** decimals))

def from_wei(amount: int, decimals: int = 18) -> float:
    """Convert wei back to decimal."""
    return amount / (10 ** decimals)

def apply_rate_limit(calls_per_second: float = 1.0) -> None:
    """Delay to respect API rate limits."""
    time.sleep(1.0 / calls_per_second)

def load_config_from_json(config_str: str) -> Dict[str, Any]:
    """Parse configuration from JSON string."""
    try:
        return json.loads(config_str)
    except (json.JSONDecodeError, TypeError):
        return {}

class CryptoHelpers:
    """Organized helpers for crypto operations after reorganization."""
    def __init__(self, default_network: str = "mainnet"):
        self.default_network = default_network
        self.transaction_log: List[Dict[str, Any]] = []

    def create_transaction(self, sender: str, receiver: str, amount: float) -> Dict[str, Any]:
        """Create a basic transaction object."""
        if not validate_address(sender) or not validate_address(receiver):
            raise ValueError("Invalid sender or receiver address")
        tx = {
            "sender": sender,
            "receiver": receiver,
            "amount_wei": to_wei(amount),
            "network": self.default_network,
            "timestamp": time.time()
        }
        self.transaction_log.append(tx)
        return tx

    def get_transaction_count(self) -> int:
        """Return number of transactions created."""
        return len(self.transaction_log)

    def export_log(self) -> str:
        """Export log as JSON string."""
        return json.dumps(self.transaction_log, indent=2)