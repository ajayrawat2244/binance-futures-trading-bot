import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from bot.logging_config import logger

BASE_URL = "https://testnet.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _generate_signature(self, params):
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256,
        ).hexdigest()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        url = BASE_URL + endpoint

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000),
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._generate_signature(params)

        headers = {
            "X-MBX-APIKEY": self.api_key,
        }

        try:
            logger.info(f"Order Request: {params}")

            response = requests.post(url, headers=headers, params=params, timeout=10)

            logger.info(f"API Response: {response.text}")

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"Network/API Error: {str(e)}")
            raise