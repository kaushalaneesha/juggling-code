class Catalog:
    def __init__(self) -> None:
        pass

    def getProductByName(name: String):
        pass

    def getProductByCategory(category: Category):
        pass

class Category:
    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id

class Item:
    def __init__(self, id: str, quantity: int) -> None:
        self.__product_id = id
        self.__quantity = quantity

class Product:
    def __init__(self, name: str, id: str, category: Category, items: Item) -> None:
        self.name = name 
        self.id = id
        self.category = category
        self.items = items

