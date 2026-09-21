from typing import List, Dict, Optional

class CryptoTransactionProcessor:
    """Handles batch processing of crypto transaction data."""

    def __init__(self, fee_rate: float = 0.001) -> None:
        self.fee_rate: float = fee_rate

    def calculate_net_amount(self, raw_amount: float) -> float:
        """Calculates net amount after applying the standard fee."""
        return raw_amount * (1 - self.fee_rate)

    def process_batch(self, transactions: List[Dict[str, float]]) -> List[float]:
        """Processes a list of transactions and returns net values."""
        results: List[float] = []
        for tx in transactions:
            amount: Optional[float] = tx.get("amount")
            if amount is not None and amount > 0:
                net: float = self.calculate_net_amount(amount)
                results.append(round(net, 8))
        return results

    def validate_tx_data(self, data: Dict[str, float]) -> bool:
        """Checks if transaction data contains valid non-negative amounts."""
        amount = data.get("amount", -1)
        return isinstance(amount, (int, float)) and amount >= 0

def main() -> None:
    processor = CryptoTransactionProcessor(fee_rate=0.005)
    sample_data: List[Dict[str, float]] = [{"amount": 1.5}, {"amount": 0.25}]
    processed: List[float] = processor.process_batch(sample_data)
    print(f"Processed totals: {processed}")

if __name__ == "__main__":
    main()