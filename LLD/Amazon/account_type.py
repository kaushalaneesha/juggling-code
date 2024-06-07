
from abc import ABC
from Amazon.catalog import Category, Product
from Amazon.constants import AccountStatus, Address
from Amazon.events import Review


class Account:
    def __init__(self, user_name: str, password: str, account_status: AccountStatus, email: str, phone_number: str, shipping_address: Address) -> None:
        self.user_name = user_name
        self.password = password
        self.account_status = account_status 
        self.__email = email 
        self.__phone_number = phone_number
        self.__shipping_address = shipping_address
        self.__credit_cards = []

    def add_product(product: Product):
        pass

    def add_review(review: Review):
        pass

    def reset_password(passwrod: str):
        pass


class Customer(ABC):
    def __init__(self, ) -> None:
        pass
    

class Member(Customer):
    def __init__(self, account: Account) -> None:
        self.account = account

    def getBillingInfo(order_id: str):
        pass

    def getOrderStatus(order: str):
        pass

class Guest(Customer):
    def register(account: Account):
        pass

class Admin:
    def createCategory(category: Category):
        pass

    def blockCustomer(customer: Customer):
        pass

