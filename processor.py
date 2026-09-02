import re
import time

def is_valid_crypto_address(address, crypto_type="eth"):
    """Validate cryptocurrency address format."""
    if crypto_type == "eth":
        pattern = r"^0x[a-fA-F0-9]{40}$"
        return bool(re.match(pattern, address))
    elif crypto_type == "btc":
        pattern = r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
        return bool(re.match(pattern, address))
    return False

def validate_input(data):
    """Perform input validation for crypto transaction."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    required_fields = ["address", "amount", "crypto_type"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    if not is_valid_crypto_address(data["address"], data["crypto_type"]):
        raise ValueError("Invalid cryptocurrency address")
    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        raise ValueError("Amount must be a positive number")
    return True

def process_transaction(transaction):
    """Simulate processing a crypto transaction."""
    print(f"Processing {transaction['crypto_type']} transaction: {transaction['address']} for {transaction['amount']}")
    time.sleep(0.05)
    return {
        "status": "success",
        "tx_id": f"tx_{int(time.time())}",
        "address": transaction["address"],
        "amount": transaction["amount"]
    }

def main_processing_loop(inputs):
    """Main loop for processing crypto inputs with validation."""
    results = []
    for idx, input_data in enumerate(inputs):
        print(f"Processing item {idx + 1}")
        try:
            validate_input(input_data)
            result = process_transaction(input_data)
            results.append(result)
        except ValueError as e:
            print(f"Input validation failed: {e}")
            results.append({"status": "failed", "error": str(e)})
        except Exception as e:
            print(f"Unexpected error: {e}")
            results.append({"status": "failed", "error": str(e)})
    return results

if __name__ == "__main__":
    sample_inputs = [
        {"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": 1.5, "crypto_type": "eth"},
        {"address": "0x123", "amount": 2.0, "crypto_type": "eth"},
        {"address": "0xabcdef1234567890abcdef1234567890abcdef12", "amount": 0, "crypto_type": "eth"},
        {"address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "amount": 0.5, "crypto_type": "btc"},
        {"address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": 10.0, "crypto_type": "eth"}
    ]
    final_results = main_processing_loop(sample_inputs)
    print("Final results:")
    for res in final_results:
        print(res)
