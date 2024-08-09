--------- EASY QUESTIONS -------------
-- 2. When do they get here? List the arrival time and the first and last names for all guests due to arrive on 2016-11-05, order the output by time of arrival.
select 
  arrival_time, 
  first_name,
  last_name
from booking
inner join guest
on booking.guest_id = guest.id
where
booking_date = '2016-11-05'
order by arrival_time
;

-- 3. Look up daily rates. Give the daily rate that should be paid for bookings with ids 5152, 5165, 5154 and 5295. Include booking id, room type, number of occupants and the amount.
SELECT 
    booking_id, 
    room_type, 
    occupants,
    amount
FROM 
    booking
    INNER JOIN rate 
    ON booking.room_type_requested = rate.room_type
    and booking.occupants = rate.occupancy
WHERE booking_id IN (5152, 5165, 5154, 5295)
;

-- Who’s in 101? Find who is staying in room 101 on 2016-12-03, include first name, last name and address.
SELECT 
    first_name, 
    last_name, 
    address
FROM 
    guest
    INNER JOIN booking 
    ON guest.id = booking.guest_id
WHERE
    booking.room_no = 101
    AND booking_date = '2016-12-03'

-- How many bookings, how many nights? For guests 1185 and 1270 show the number of bookings made and the total number of nights. Your output should include the guest id and the total number of bookings and the total number of nights.
SELECT 
    guest_id, 
    COUNT(nights),
    SUM(nights)
FROM 
    booking
WHERE
    guest_id IN (1185, 1270)
GROUP BY 
    guest_id
;


------------ MEDIUM QUESTIONS --------------------

-- Ruth Cadbury. Show the total amount payable by guest Ruth Cadbury for her room bookings. 
SELECT 
    SUM(amount*nights)
FROM 
    rate
    INNER JOIN booking
    ON rate.room_type = booking.room_type_requested
    AND rate.occupancy = booking.occupants
    INNER JOIN guest ON 
    booking.guest_id = guest.id
    AND guest.first_name = 'Ruth'
    AND guest.last_name = 'Cadbury'
;

-- Including Extras. Calculate the total bill for booking 5346 including extras.
WITH extra_amount AS (
    SELECT 
        SUM(amount) AS extra_amount
    FROM 
        extra
    WHERE
        booking_id = 5346
), booking_amount AS (
SELECT 
    SUM(rate.amount*nights) as booking_amount
FROM 
    rate
    INNER JOIN booking
    ON rate.room_type = booking.room_type_requested
    AND rate.occupancy = booking.occupants
WHERE 
    booking.booking_id = 5346 
)
SELECT extra_amount + booking_amount from extra_amount, booking_amount;

-- Edinburgh Residents. For every guest who has the word “Edinburgh” in their address show the total number of nights booked. Be sure to include 0 for those guests who have never had a booking. Show last name, first name, address and number of nights. Order by last name then first name.
SELECT 
    last_name, 
    first_name, 
    address,
    IFNULL(SUM(nights), 0)
FROM 
    guest
    LEFT JOIN booking 
    ON guest.id = booking.guest_id
WHERE
    guest.address LIKE '%Edinburgh%'
GROUP BY 
    first_name, last_name, address
ORDER BY last_name, first_name
;

-- How busy are we? For each day of the week beginning 2016-11-25 show the number of bookings starting that day. Be sure to show all the days of the week in the correct order.
SELECT 
    booking_date,
    COUNT(booking_id)
FROM
    booking
WHERE booking_date BETWEEN '2016-11-25' AND '2016-12-01'
GROUP BY 
    booking_date
ORDER BY 
    booking_date
;

-- How many guests? Show the number of guests in the hotel on the night of 2016-11-21. Include all occupants who checked in that day but not those who checked out.
SELECT 
    SUM(occupants)
from 
    booking
where
    booking_date <= '2016-11-21'
    AND DATE_ADD(booking_date, INTERVAL nights DAY) > '2016-11-21'
;

-- Coincidence. Have two guests with the same surname ever stayed in the hotel on the evening? Show the last name and both first names. Do not include duplicates.


WITH bookings_with_guests AS (
select 
    booking_id, booking_date, nights, guest_id, first_name, last_name
FROM booking
INNER JOIN guest
WHERE booking.guest_id = guest.id
)
SELECT DISTINCT bg1.last_name, bg1.first_name, bg2.first_name 
FROM bookings_with_guests bg1
INNER JOIN bookings_with_guests bg2
WHERE bg1.last_name = bg2.last_name
AND bg1.guest_id < bg2.guest_id
AND (((bg1.booking_date BETWEEN bg2.booking_date AND DATE_ADD(bg2.booking_date, INTERVAL bg2.nights  - 1 DAY)) OR ((bg2.booking_date BETWEEN bg1.booking_date AND DATE_ADD(bg1.booking_date, INTERVAL bg1.nights  - 1 DAY))))
)
order by bg1.last_name
;

-- Check out per floor. The first digit of the room number indicates the floor – e.g. room 201 is on the 2nd floor. For each day of the week beginning 2016-11-14 show how many rooms are being vacated that day by floor number. Show all days in the correct order.
SELECT 
    DATE_ADD(booking_date, INTERVAL nights DAY) AS i,
    SUM(CASE WHEN room_no LIKE '1%' THEN 1 ELSE 0 END) AS 1st, 
    SUM(CASE WHEN room_no LIKE '2%' THEN 1 ELSE 0 END) AS 2nd, 
    SUM(CASE WHEN room_no LIKE '3%' THEN 1 ELSE 0 END) AS 3rd
FROM 
    booking
WHERE
    DATE_ADD(booking_date, INTERVAL nights DAY) >= '2016-11-14'
    AND DATE_ADD(booking_date, INTERVAL nights DAY) < '2016-11-21'
GROUP BY 
    i
;

-- Free rooms? List the rooms that are free on the day 25th Nov 2016.
SELECT 
    id
FROM 
    room 
LEFT JOIN booking
ON room.id = booking.room_no
WHERE 
    booking.booking_dae 