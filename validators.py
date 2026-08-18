import re

# Regular expression for validating cryptocurrency addresses
BTC_ADDRESS_REGEX = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
ETH_ADDRESS_REGEX = r'^0x[a-fA-F0-9]{40}$'

def is_valid_btc_address(address: str) -> bool:
    """
    Validate if the provided Bitcoin address is valid.
    Bitcoin addresses can start with '1' or '3' and must be 26-35 characters long.
    """
    return bool(re.match(BTC_ADDRESS_REGEX, address))


def is_valid_eth_address(address: str) -> bool:
    """
    Validate if the provided Ethereum address is valid.
    Ethereum addresses must start with '0x' followed by 40 hexadecimal characters.
    """
    return bool(re.match(ETH_ADDRESS_REGEX, address))


def validate_crypto_address(address: str, crypto_type: str) -> bool:
    """
    Validate a cryptocurrency address based on the specified type.
    Type can be 'btc' for Bitcoin or 'eth' for Ethereum.
    """
    if crypto_type == 'btc':
        return is_valid_btc_address(address)
    elif crypto_type == 'eth':
        return is_valid_eth_address(address)
    else:
        raise ValueError("Unsupported cryptocurrency type. Use 'btc' or 'eth'.")