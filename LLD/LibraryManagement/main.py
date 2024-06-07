from account_type import *
from book import *
from order import *


book = Book("book1", "Never Give Up", "Aneesha", "self-help", 4)
bookItem1 = BookItem("1", book, BookStatus.AVAILABLE)
bookItem2 = BookItem("2", book, BookStatus.AVAILABLE)
bookItem3 = BookItem("3", book, BookStatus.AVAILABLE)
bookItem4 = BookItem("4", book, BookStatus.AVAILABLE)
available_books = {book: [bookItem1, bookItem2, bookItem3, bookItem4]}

catalog = Catalog(available_books)
member = Member("AA")

ordMngr = OrderManager(catalog)
ordMngr.create_order("222", member, [book])
for book, bookItems in catalog.available_books.items():
    print(book)
    for bk in bookItems:
        print(bk)