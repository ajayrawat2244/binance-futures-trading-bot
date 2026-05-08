from bot.validators import validate_order
from bot.client import BinanceFuturesClient


class OrderService:
    def __init__(self, api_key, api_secret):
        self.client = BinanceFuturesClient(api_key, api_secret)

    def create_order(self, symbol, side, order_type, quantity, price=None):
        validate_order(symbol, side, order_type, quantity, price)

        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )