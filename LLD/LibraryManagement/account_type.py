from abc import ABC


class Account:
    def __init__(self, id: str, password: str) -> None:
        self.__password = password
        self.__id = id

class Person(ABC):

    def __init__(self, name, account, address, email, phone_number) -> None:
        self.__name = name
        self.__account = account
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number

class Member(Person):
    def __init__(self, name) -> None:
        self._name = name

class Admin(Person):
    def __init__(self, name, account, address, email, phone_number, catalog) -> None:
        super().__init__(name, account, address, email, phone_number)
        self._catalog = catalog

    # methods to update the catalog
    def add_book(book): 
        pass

    def remove_book(book):
        pass

    def update_book(book):
        pass