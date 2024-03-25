from abc import ABC
from typing import List

class ParkingFloor:
    def __init__(self, number, slots, capacity) -> None:
        self._number = number
        self._slot = slots
        self._capacity = capacity

class ParkingTicket:
    pass

class Gate(ABC):
    def __init__(self) -> None:
        self._id = id 

class Entry(Gate):
    def __init__(self, id) -> None:
        super().__init__(id)

    def get_parking_ticket(vehicle) -> ParkingTicket:
        pass

class ExitGate(Gate):
    def __init__(self, id) -> None:
        super().__init__(id)

    def pay_for_parking(parkingTicket, payment_type) -> ParkingTicket:
        pass
     

class ParkingLot:
    def __init__(self, address, id, entries: List[Entry], exits: List[ExitGate]) -> None:
        self._address = address
        self._id = id
        self._parking_floors = None
        self._entry_points = entries # List of entry gates
        self._exit_points = exits # List of exit gates


    def add_floor(self, parkingfloor):
        pass

    def getCapacity(self, slotType, vehicleType):
        total = 0
        for floor in self._parking_floors:
            total += floor.get_available_capacity(slotType, vehicleType)
        return total
    
    def is_space_available(vehicle):
        pass
    



