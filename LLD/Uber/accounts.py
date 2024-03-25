from abc import ABC
from enum import Enum

from payment import PaymentType

class Address:
    def __init__(self, city: str, country: str, pincode: str, state: str, street: str): 
        self.__city = city
        self.__country = country
        self.__pincode = pincode
        self.__state = state
        self.__street = street

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class Account:
    def __init__(self, id: str, password: str, status: AccountStatus) -> None:
        self.__password = password
        self.__id = id
        self.__status = status

class Person(ABC):

    def __init__(self, name, account, addresses, email, phone_number) -> None:
        self.__name = name
        self.__account = account
        self.__addresses = addresses
        self.__email = email
        self.__phone_number = phone_number

class Rider(Person):
    def __init__(self, name, account, addresses, email, phone_number) -> None:
        super().__init__(name, account, addresses, email, phone_number)
        # All the past bookings of this user
        self.__bookings = None
        self.__payment_methods = set()

    def add_payment_method(self, pt: PaymentType):
        self.__payment_methods.add(pt)

    def make_booking(self, booking):
        pass

    def cancel_booking(self, booking):
        pass

    def make_payment(self, booking):
        booking.payment.status = 1

class Driver(Person):
    def __init__(self, ride, name, account, addresses, email, phone_number) -> None:
        super().__init__(name, account, addresses, email, phone_number)
        self.__ride = ride # Assuming one driver has one ride
        self.__bookings = None
        self.__earnings = None # total earning by all the bookings
        self.__rating = None # average rating of all its bookings

    def accept_booking(self, booking):
        booking.driver = self

    def reject_booking(self, booking):
        pass

    def update_earing(self, booking):
        self.__earning += booking.payment.price *.08

class Admin(Person):
    pass
