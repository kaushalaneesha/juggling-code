from ast import List
from constants import Address, SeatType, Status
from movie import Show

class CinemaHall:

    def __init__(self, name: str, id: str, address: Address, audis: List[Audi]):
        self.name = name
        self.id = id
        self.address = address
        self.audis = audis # List of screens

class Audi:
    def __init__(self, id, name, total_seats, shows: List[Show]) -> None:
        self.__id = id
        self.__name = name
        self.__total_seats = total_seats 
        self.__shows = shows

class Seat:
    def __init__(self, id: str, status: Status, price: float, seat_type: SeatType):
        self.__id = id
        self.__status = status
        self.__price = price
        self.__seat_type = seat_type
