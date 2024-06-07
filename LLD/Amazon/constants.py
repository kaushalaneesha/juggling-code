from enum import Enum

class Address:
    def __init__(self, pincode, city, state, country, street) -> None:
        self.__pincode = pincode
        self.__street = street
        self.__city = city
        self.__country = country
        self._state = state

class OrderStatus: 
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELLED, REFUND_APPLIED  = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, REGISTERED, ARCHIEVED, BLOCKED, UNKNOWN = 1, 2, 3, 4, 5

class ShippingStatus(Enum):
    PENDING, SHIPPED, DELIVERED, ON_HOLD = 1, 2, 3, 4 

class Rating(Enum):
    One, Two, Three, Four, Five = 1, 2, 3, 4, 5 

class PaymentStatus(Enum): 
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


