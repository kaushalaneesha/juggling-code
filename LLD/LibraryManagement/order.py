
import datetime
from typing import List, Self
import uuid

from book import Book, BookStatus


class Order:
    def __init__(self, id, bookItems, date: datetime, member) -> None:
        self._id = id
        self._books = bookItems
        self._date = date
        self._member = member

class OrderManager:
    _instance = None

    def __init__(self, catalog) -> None:
        self.__catalog = catalog

    def __new__(cls, catalog) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__catalog = catalog
        return cls._instance
    
    
    def create_order(self, date, member, books: List[Book]) -> Order:
        bookItems = []
        for book in books:
            if self.__catalog.available_books[book]:
                # pop from avaialble books
                bookItem = self.__catalog.available_books[book].pop()
                bookItems.append(bookItem)
        return Order(uuid.uuid4(), bookItems, date, member)

class ReservationManager:
    _instance = None

    def __init__(self, catalog) -> None:
        self.__catalog = catalog

    def __new__(cls) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def reserve_book(self, date, member, books: List[Book]):
        bookItems = []
        for book in books:
            if self.__catalog.available_books[book]:
                self.__catalog.available_books[book][0].book_status = BookStatus.RESERVED
                pass
                # mark the first available book item as reserved
                # bookItem.book_status = BookStatus.RESERVED
        # Notify if none found
        