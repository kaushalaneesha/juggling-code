from abc import ABC
from typing import Self
import uuid


class Booking:
    def __init__(self) -> None:
        self.id = None
        self.date = None
        self.customer = None 
        self.hotel = None
        self.room = None
        self.guests = None
        self.status = None
        self.ammenities = None
        self.service = None

class BookingBuilder:
    def __init__(self) -> None:
        self.booking = None
    
    def add_amenitites(self, ammenities):
        self.booking.ammenities = ammenities

    def add_service(self, service):
        self.booking.service.append(service)

# Can also query database have kept it an in memory map for now
class BookingCatalog:
    instance = None

    def __init__(self) -> None:
        self.bookings = {} # map of booking id to booking

    def __new__(cls) -> Self:
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

class NotificationSender(ABC):
    def sendNotification(self, user_id, booking_id, mesg):
        pass

class SMSNotificationSender(NotificationSender):

    def sendNotification(self, user_id, booking_id, mesg):
        print("User: {} Booking: {} Mesg: {}".format(user_id, booking_id, mesg))


class NotificationManager():
    def __init__(self) -> None:
        self._senders = {}

    def addSender(self, userId, sender: NotificationSender):
        if userId not in self._senders:
            self._senders[userId] = [sender]
        else:
            self._senders[userId].append(sender)

    def notify(self, userId, booking_id, mesg):
        for sender in self._senders[userId]:
            sender.sendNotification(userId, booking_id, mesg)

class BookingService:
    instance = None

    def __new__(cls) -> Self:
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self._booking_catalog = BookingCatalog()
        self._notification_manager = NotificationManager()

    def create_booking(self, booking: Booking):
        booking.id = uuid.uuid4()
        self._booking_catalog.bookings[booking.id] = booking
        # Add user for updates
        self._notification_manager.addSender("123", SMSNotificationSender())
        
        # also send notification booking created
        self._notification_manager.notify("123", booking.id, "Booking created")

    def cancel_booking(self, bookingId: str):
        self._booking_catalog.remove(bookingId)

    def update_booking(self, bookingId: str, booking: Booking):
        self._booking_catalog[bookingId] = booking

    def get_booking(self, bookingId):
        return self._booking_catalog[bookingId]
    

booking = BookingBuilder()
booking2 = BookingBuilder()
bkService = BookingService()
bkService.create_booking(booking)
bkService.create_booking(booking2)


