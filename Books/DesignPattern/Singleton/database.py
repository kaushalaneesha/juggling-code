# database is a singleton class
from typing import Self


class DataBase:
    _instance = None

    def __new__(cls) -> Self:
        print("this is new")
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def query(self):
        print("Querying database with address {}".format(id(self)))

    def __init__(self) -> None:
        print("This is init")
    
db = DataBase()
db2 = DataBase()
print(db is db2)
db.query()
db2.query()