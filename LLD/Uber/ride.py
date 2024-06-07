from enum import Enum
from typing import List

class RideStatus(Enum):
    Booked, Cancelled = 1, 2

class Ride:
    def __init__(self, ride_number, ride_type, driver) -> None:
        self.__ride_number = ride_number
        self.__driver = driver

class Car(Ride):
    def __init__(self, ride_number, ride_type, driver, company) -> None:
        super().__init__(ride_number, ride_type, driver)
        self.__company = company # Honda city, Indica etc

class Auto(Ride):
    def __init__(self, ride_number, ride_type, driver) -> None:
        super().__init__(ride_number, ride_type, driver)

class Booking:
    def __init__(self, id, booked_by, passengers, source, destination, status, ride) -> None:
        self.__id = id 
        self.__booked_by = booked_by
        self.__passengers = passengers
        self.__source = source
        self.__destination = destination 
        self.__status = status
        self.__ride = ride

        self.__rating = None
        self.__payment = None

