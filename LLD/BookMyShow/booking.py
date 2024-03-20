from ast import List
import datetime

from cinema import Audi, Seat
from constants import SeatType, Status
from movie import Movie, Show

class Payment:
    def __init__(self, amount, transaction_id, payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status

class Booking:

    def __init__(self, id: str, status: Status, show: Show, audi: Audi, seats: List[Seat], payment: Payment) -> None:
        self.__id = id 
        self.__show = show
        self.__audi = audi
        self.__seats = seats
        self.__booking_status = status
        self.__payment = payment

    def make_payment(payment: Payment):
        pass

    def cancel():
        pass

    def assign_seats():
        pass




    