from typing import Any, Dict


def validate_address(address: str) -> bool:
    """
    Validate if the given address is a valid cryptocurrency address.

    Args:
        address (str): The cryptocurrency address to validate.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Basic validation rules for an address
    if len(address) < 26 or len(address) > 42:
        return False
    if not all(c in "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz" for c in address):
        return False
    return True


def validate_transaction(transaction: Dict[str, Any]) -> bool:
    """
    Validate if the given transaction data is valid.

    Args:
        transaction (Dict[str, Any]): The transaction data to validate.

    Returns:
        bool: True if the transaction is valid, False otherwise.
    """
    required_keys = {'from', 'to', 'amount', 'fee', 'nonce'}
    if not required_keys.issubset(transaction.keys()):
        return False
    if not isinstance(transaction['amount'], (int, float)):
        return False
    return True


if __name__ == "__main__":
    # Example usage
    print(validate_address("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))  # True
    print(validate_transaction({"from": "addr1", "to": "addr2", "amount": 0.01, "fee": 0.001, "nonce": 1}))  # True