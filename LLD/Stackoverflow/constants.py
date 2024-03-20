from enum import Enum

# Add all the enums and constants related to booing

class Address:
    def __init__(self, city: str, country: str, pincode: str, state: str, street: str): 
        self.__city = city
        self.__country = country
        self.__pincode = pincode
        self.__state = state
        self.__street = street

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6