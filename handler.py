import logging
import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

def execute_trade(api_client, pair: str, amount: float):
    """Executes crypto trade with network and validation safety."""
    if amount <= 0:
        logger.error(f"invalid trade amount: {amount}")
        return None

    try:
        response = api_client.post("/trade", json={"pair": pair, "amount": amount})
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.warning(f"network failure for {pair}: {e}")
        return None
    except ValueError as e:
        logger.error(f"malformed api response: {e}")
        return None
    except Exception as e:
        logger.critical(f"unexpected system error: {type(e).__name__}")
        raise

def validate_balance(balance: dict, required: float):
    """Checks funds before order placement."""
    try:
        available = float(balance.get('available', 0))
        if available < required:
            raise ValueError("insufficient funds")
        return True
    except (TypeError, ValueError):
        logger.error("invalid balance data structure")
        return False