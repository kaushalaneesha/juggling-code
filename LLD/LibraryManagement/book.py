from enum import Enum
from typing import Dict, List, Self


class Book:
    def __init__(self, uid, name, author, genre, quantity) -> None:
        self._uid = uid
        self._name = name
        self._author = author
        self._genre = genre
        self._quantity = quantity

    def __str__(self) -> str:
        return "{} {} {}".format(self._name, self._author, self._genre)

    
class BookStatus(Enum):
    AVAILABLE, RESERVED, BORROWED = 1, 2, 3

class BookItem:
    def __init__(self, id, book, status) -> None:
        self._book = book
        self._id = id
        self._status = status

    def __str__(self) -> str:
        return "{} {} {}".format(self._status, self._book._name, self._book._author, self._book._genre)

class Catalog:
    _instance = None
    def __new__(cls, available_books: Dict[Book, List[BookItem]]) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.available_books = available_books
        return cls._instance

    def __init__(self, available_books: Dict[Book, List[BookItem]]) -> None:
        self.available_books = available_books