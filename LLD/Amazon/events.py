from ast import List
from Amazon.account_type import Customer, Member
from Amazon.catalog import Item, Product
from Amazon.constants import Address, OrderStatus, Rating


class Review:
    def __init__(self, id: str, rating: Rating, comments: str, user: Member) -> None:
        self.__id = id
        self.__rating = rating
        self.__comments  = comments
        self.__user = user

class Order:
    def __init__(self, id: str, products: List[Item], order_total: float, shipping_address: Address, user: Member, status: OrderStatus) -> None:
        self.__id = id
        self.__products = products       # will have product id and quantity
        self.__order_total = order_total 
        self.__shipping_address = shipping_address
        self.__user = user
        self.__order_status = status

class Cart:
    def __init__(self, items: List[Item], user: Customer, cart_value: float):
        self.__items = items
        self.__user = user
        self.__cart_value = cart_value

class Payment:
    def __init__(self, status, price: float, user: Member, order_id: str) -> None:
        self.status = status
        self.__price = price 
        self.__user = user
        self.__order_id = order_id
        

