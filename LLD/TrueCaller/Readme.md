# True caller

## Design True caller / WhosCall / Showcaller

Come up with application that can perform  
* Caller identification  
* Call blocking  
* Spam Detection
* Store users contacts  
* Search for users contacts by name and number 

### Use cases

1. Users should be able to register
2. Users should be able to add contacts
3. Users should be able to import contacts  
4. Users should be able to block contacts
5. Users should be able to report spam
6. Users should be able to unblock numbers
7. Users should be notified when suspected junk caller calls (??)
8. Users should be able to identify caller when call comes
9. Users should be able to upgrade to premium plans
10. Users should be able to search for contacts by name 
11. Users should be able to search for contacts by number
12. Users should be able to add business (??)
13. Post registration and addition of contacts register with global directory.
14. Users should be able to search from global directory

### Entities

* Admin
* Search 
    - Search by name
    - Search by number (call identifcation)
* Account
    - name 
    - email
    - phone number
    - last active
    - accountType: AccountType
* AccountType
    - Standard
    - Premimum
* Customer
    * Guest
    * Member
        - account: Account
        - valid_contact: PhoneNumbers # List of contact added manually or imported
        - blocked_contacts: PhoneNumbers # list of contacts blocked (status: BLOCKED)
        - marked_spam: PhoneNumbers # List of contacts marked spam (status: SPAM)
        - functions
           - Add contact
           - Import contacts
           - block contacts
* Contact
    - name
    - phone_number: PhoneNumber
* Vertical
    - Donation
    - School
    - Retail
    - Bank
    - Fraud
    - Unknown
* PHoneNumberType
    - Business 
    - Personal
* PhoneNumberStatus
    - SPAM
    - LIKELY SPAM
    - VALID
    - IN CONTACT
    - BLOCKED
* PhoneNumber
    - isd
    - extension
    - number
    - status: PhoneNumberStatus
    - type: PhoneNumberType
    - vertical: Vertical
    - contact: Contact (Name of contact/owner)


DataBase
- Phone numbers 
- How will we merge the names?