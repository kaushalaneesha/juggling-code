from enum import Enum


class PaymentStatus(Enum):
    Accepted, Declined, Pending = 1, 2, 3

class PaymentType(Enum):
    Card, Cash, Wallet = 1, 2, 3

class Payment:
    def __init__(self, id, price, payment_type, payment_status) -> None:
        self.__id = id
        self.__price = price
        self.__payment_type = payment_type
        self.__payment_status = payment_status
