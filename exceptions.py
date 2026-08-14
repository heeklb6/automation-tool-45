class CryptoError(Exception):
    """Base class for exceptions in this module."""
    pass

class InsufficientFundsError(CryptoError):
    """Exception raised for insufficient funds."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f'Insufficient funds: Tried to withdraw {amount}, but balance is {balance}.')

class TransactionError(CryptoError):
    """Exception raised for transaction failures."""
    def __init__(self, transaction_id, reason):
        self.transaction_id = transaction_id
        self.reason = reason
        super().__init__(f'Transaction {transaction_id} failed: {reason}.')

class NetworkError(CryptoError):
    """Exception raised for network-related issues."""
    def __init__(self, message):
        super().__init__(f'Network error: {message}.')

# Example functions demonstrating error handling

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount


def process_transaction(transaction_id):
    # Simulating a transaction failure
    raise TransactionError(transaction_id, 'Insufficient liquidity')

# Simulate network function
def fetch_data():
    raise NetworkError('Could not connect to server')
