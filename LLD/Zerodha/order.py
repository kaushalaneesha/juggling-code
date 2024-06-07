from typing import Self

from constants import TransactionType
from user import UserCatalog


class Order:
    def __init__(self, transaction_type, order_type, exhange_type, stock, quantity, price) -> None:
        self.order_type = order_type
        self.transaction_type = transaction_type
        self._order_type = order_type
        self._stock = stock
        self._quantity = quantity
        self._price = price # Why is this needed here? 
        self._exchange = exhange_type
    
    # add getters and setters
    def get_exchange_type(self):
        return self._exchange
    
class OrderValidator:
    def __init__(self) -> None:
        pass

    def validateOrder(self, userId: str, order: Order) -> bool:
        # get user
        user = UserCatalog.get_user(userId)
        if order.get_exchange_type() == TransactionType.BUY:
            # check funds 
            print("check if funds are enought")
        else:
            print("check if potfolio has the stock to sell")
        # validate
        return True
    
class ExchangeConnector:
    _instance = None
    def __new__(cls) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        # connection to exchange
        pass

    def place_order_to_exchange(self, userId, order):
        print("Order placed to exchange. Congratulations!")
        return True

class OrderExecutioner:
    def __init__(self) -> None:
        pass

    def place_order(self, userId: str, order: Order) -> bool:
        order_exchange = ExchangeConnector()
        return order_exchange.place_order_to_exchange(userId, order)
        # update funds for the user if successful

class OrderManager:
    _instance = None

    # class to manage orders
    def __init__(self) -> None:
        self._order_validator = OrderValidator()
        self._order_executioner = OrderExecutioner()

    def __new__(cls) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def place_order(self, order: Order, userId: str):
        if self._order_validator.validateOrder(userId, order):
            self._order_executioner.place_order(userId, order)
        return None



