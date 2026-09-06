import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class TradeProcessor:
    SUPPORTED_SYMBOLS = {"BTC", "ETH", "SOL", "USDT"}

    def __init__(self, min_order_usd=10.0, max_order_usd=50000.0):
        self.min_order_usd = min_order_usd
        self.max_order_usd = max_order_usd

    def validate_trade_signal(self, signal: dict) -> bool:
        """Validates raw signal payload prior to execution."""
        if not isinstance(signal, dict):
            raise ValueError("Payload must be a dictionary")

        symbol = signal.get("symbol")
        if not symbol or symbol not in self.SUPPORTED_SYMBOLS:
            raise ValueError(f"Unsupported symbol: '{symbol}'")

        side = signal.get("side")
        if side not in {"BUY", "SELL"}:
            raise ValueError(f"Invalid side: '{side}'. Must be BUY or SELL")

        amount = signal.get("amount")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError(f"Invalid trade amount: {amount}")

        price = signal.get("price")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError(f"Invalid trade price: {price}")

        total_value = amount * price
        if not (self.min_order_usd <= total_value <= self.max_order_usd):
            raise ValueError(f"Order value ${total_value:.2f} out of bounds")

        return True

    def process_signals(self, raw_signals: list) -> int:
        """Iterates over incoming signals, enforcing input validation before execution."""
        successful_orders = 0
        for idx, signal in enumerate(raw_signals, start=1):
            try:
                self.validate_trade_signal(signal)
                logging.info(f"Processing [{idx}/{len(raw_signals)}]: {signal['side']} {signal['amount']} {signal['symbol']}")
                successful_orders += 1
            except ValueError as err:
                logging.warning(f"Skipping invalid signal [{idx}/{len(raw_signals)}]: {err}")
                continue

        return successful_orders
