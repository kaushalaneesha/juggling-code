from constants import ExchangeType


class Stock:
    def __init__(self, name: str, exchange_type: ExchangeType, price: float) -> None:
        self._name = name
        self._exchange = exchange_type 
        self._price = price 

    def update_price(self, price):
        self._price = price 

class MarketData:
    def __init__(self) -> None:
        self._stocks = None # Map of stock id to current price