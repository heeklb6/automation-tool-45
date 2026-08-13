import json
from validators import validate_input

class CryptoAutomation:
    def __init__(self, config):
        self.config = config

    def process_transactions(self, transactions):
        results = []
        for transaction in transactions:
            if not validate_input(transaction):
                results.append({'status': 'error', 'message': 'Invalid transaction', 'transaction': transaction})
                continue

            result = self.execute_transaction(transaction)
            results.append({'status': 'success', 'result': result})
        return results
    
    def execute_transaction(self, transaction):
        # Placeholder for executing the crypto transaction.
        return {'id': transaction['id'], 'status': 'completed'}

if __name__ == '__main__':
    sample_transactions = [
        {'id': 1, 'amount': 0.5, 'currency': 'BTC'},
        {'id': 2, 'amount': -0.1, 'currency': 'ETH'},  # Invalid transaction
        {'id': 3, 'amount': 2, 'currency': 'LTC'}
    ]
    automation = CryptoAutomation(config={})
    print(json.dumps(automation.process_transactions(sample_transactions), indent=4))