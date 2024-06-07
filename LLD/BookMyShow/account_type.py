# Contains all kinds of person that interact with booking system

# Account (account of any person)
# Person (generic person class). Below are the types of persons
#   Admin 
#   Customer

from abc import ABC
from ast import List
from booking import Booking
from constants import AccountStatus
from movie import Movie


class Account:
    def __init__(self, id: str, password: str, status: AccountStatus) -> None:
        self.__password = password
        self.__id = id
        self.__status = status

class Person(ABC):

    def __init__(self, name, account, address, email, phone_number) -> None:
        self.__name = name
        self.__account = account
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number


class Customer(Person):

    def __init__(self, name, account, address, email, phone_number) -> None:
        super().__init__(name, account, address, email, phone_number)

    def make_booking(self, booking) -> None:
        pass

    def get_booking(self, booking_id) -> Booking:
        pass

    def get_bookings(self) -> List[Booking]:
        pass

class Admin(Person):

    def add_movie(self, movie: Movie):
        pass

    def add_show(self, show: Show):
        pass
    