# Contains all kinds of person that interact with booking system

# Account (account of any person)
# Person (generic person class). Below are the types of persons
#   Admin 
#   Customer

from abc import ABC
from typing import List
from entity import Question
from constants import AccountStatus
from search import Search


class Account:
    def __init__(self, username: str, password: str, status: AccountStatus) -> None:
        self.__password = password
        self.__username = username
        self.__status = status

class Person(ABC):

    def __init__(self, name, account, address, email, phone_number) -> None:
        self.__name = name
        self.__account = account
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number

class Guest:
    def __init__(self, id) -> None:
        self.__id = id
        self.__search = None

    def getQuestions(search: Search) -> List[Question]:
        # Run a search based on the search query and return the list of questions. 
        # Questions will have content and list of tags that will help with the search
        pass


class Member(Person, Guest):

    def __init__(self) -> None:
        self.__comments = None
        self.__answers = None
        self.__questions = None

class Admin(Person):
    pass