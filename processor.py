import logging
from decimal import Decimal, InvalidOperation

logger = logging.getLogger(__name__)

class CryptoProcessor:
    def __init__(self, exchange_client):
        self.client = exchange_client

    def execute_trade(self, symbol: str, amount: str, price: str) -> dict:
        try:
            qty = Decimal(amount)
            rate = Decimal(price)
            
            if qty <= 0 or rate <= 0:
                raise ValueError(f"Invalid trade parameters: {amount} at {price}")

            response = self.client.place_order(symbol, qty, rate)
            return {"status": "success", "txid": response.get("id")}

        except InvalidOperation:
            logger.error(f"Decimal conversion failure for {amount} or {price}")
            return {"status": "error", "message": "invalid numeric format"}
        except ValueError as e:
            logger.warning(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}
        except ConnectionError:
            logger.critical("Exchange connectivity lost during trade execution")
            return {"status": "error", "message": "network partition"}
        except Exception as e:
            logger.exception("Unexpected error in trade processor")
            return {"status": "error", "message": "internal processor failure"}

    def validate_balance(self, asset: str) -> bool:
        try:
            balance = self.client.get_balance(asset)
            return float(balance) > 0
        except (KeyError, TypeError, ConnectionError) as e:
            logger.error(f"Balance check failed for {asset}: {e}")
            return False