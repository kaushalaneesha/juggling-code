Requirements
1. Book a slot / Cancel / Update / View
    - Title
    - Set time start,end time
    - Invite people
    - Add description
    - Recurring meeting

Calender: 
    - color
    - events

Entities
- Event
    - starttime
    - endtime 
    - recuring_frequency 
    - whole_day
    - guests
    - organiser
    - description
    - title
    - id

    - update_event()
    - view_event()
    - cancel_event()


- User 
    - profile
    - calenders

APIs
- create_event(userId, details)
- cance_event(userId, eventId)
- update_Event(userId, eventId, details) 
- view_event(userId, eventId)





## For Future

1. Book a slot / Cancel / Update
    - Title
    - Set time start,end time
    - Invite people
    - Add description
    - Add location
    - Add meeting link
    - Add/set Notification 
    - Categorize the invite
    - Rely necessary 
    - Recurring meeting
2. See various calenders
3. See various displays(Week, month, workweek)
4. Create Task