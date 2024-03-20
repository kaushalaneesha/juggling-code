from LLD.Sports.constants import AccountStatus, Address


class Account:
    def __init__(self, user_name: str, password: str, account_status: AccountStatus, email: str, phone_number: str, address: Address) -> None:
        self.user_name = user_name
        self.password = password
        self.account_status = account_status 
        self.__email = email 
        self.__phone_number = phone_number
        self.__address = address
        self.__credit_cards = []

    def update_account():
        pass


class Admin:
    def __init__(self, account: Account) -> None:
        self.__account = account