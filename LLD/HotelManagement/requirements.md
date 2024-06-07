We’ll focus on the following set of requirements while designing the Hotel Management System:

The system should support the booking of different room types like standard, deluxe, family suite, etc.
Guests should be able to search the room inventory and book any available room.
The system should be able to retrieve information, such as who booked a particular room, or what rooms were booked by a specific customer.
The system should allow customers to cancel their booking - and provide them with a full refund if the cancelation occurs before 24 hours of the check-in date.
The system should be able to send notifications whenever the booking is nearing the check-in or check-out date.
The system should maintain a room housekeeping log to keep track of all housekeeping tasks.
Any customer should be able to add room services and food items.
Customers can ask for different amenities.
The customers should be able to pay their bills through credit card, check or cash.

APIs

User (Customer)
searchRoom() # various filters like date, location, hotel, room type etc
bookRoom(booking: Booking)
cancelBooking(bookingId: str)
makePayment(bookingId: str, paymentMethod: str)
addAmenitities(bookingId, amenitiies: List[amenities])
addRoomService(bookingid, foodItems)

System
getBookingByRoom(room: Room) -> Booking
getBookingByCustomer(customerId) -> Booking
giveRefund(cancelation_date: datetime, bookingId)
getHouseKeepingLog(room: Room)


Admin
addHotel ... (not covering admin for now)


Entities

Customer
    - id
    - bookings: List[str] # booking ids

Booking
- id
- date
- customer
- hotel
- room
- num_of_guests
- status: PAID, UNPAID, CANCELLED, 

Hotel
- id
- name
- address
- rooms: List[Rooms]


Room
- id
- hotel
- room_type
- price
- capacity

StandardRoom(Room)
- price
- capacity

... (other room types)

Delux(Room)

Task
- id
- hotel
- description

BookingService
- createBooking()
  - notificationmgr.addNotificationSender(customerId, SMSNotificationSender)
- cancelBooking()
- updateBooking() # ammenitites, payment etc
- deleteBooking()
- searchByRoom(room)
- searchByCustomer(customer)
- checkifNearCheckout() # check if now is near checkin or checkout call notificationmgr.notify(customerId, bookingId)

CustomerService
addCustomer(customer)
removeCustomer()
makePayment(booking, paymentMethod)

NotificationMgr
observers 
addNotificationSender
removeNotificationSender()
notify(bookingId)

NotificationSender (Observer)
send_notification()