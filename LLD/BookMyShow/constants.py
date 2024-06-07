from enum import Enum

# Add all the enums and constants related to booing

class Address:
    def __init__(self, city: str, country: str, pincode: str, state: str, street: str): 
        self.__city = city
        self.__country = country
        self.__pincode = pincode
        self.__state = state
        self.__street = street

class SeatType(Enum):
    DELUX = 1
    VIP = 2
    ECONOMY = 3
    OTHER = 4

class Status(Enum):
    BOOKED = 1
    AVAILABLE = 2
    NOT_AVAILABLE = 3
    RESERVEED = 4

class PaymentStatus(Enum): 
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6