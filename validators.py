import re

# crypto-specific validation patterns
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')
TX_HASH_PATTERN = re.compile(r'^0x[a-fA-F0-9]{64}$')

def validate_eth_address(address: str) -> bool:
    """verify ethereum address format"""
    return bool(ADDRESS_PATTERN.match(address))

def validate_tx_hash(tx_hash: str) -> bool:
    """verify transaction hash format"""
    return bool(TX_HASH_PATTERN.match(tx_hash))

def validate_amount(amount: str) -> bool:
    """verify numeric string precision for crypto balances"""
    try:
        value = float(amount)
        return value >= 0
    except ValueError:
        return False

def sanitize_input(data: str) -> str:
    """remove non-alphanumeric noise from inputs"""
    return re.sub(r'[^a-zA-Z0-9]', '', data)

def check_gas_limit(limit: int) -> bool:
    """bounds check for network gas limits"""
    return 21000 <= limit <= 10000000