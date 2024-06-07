from abc import ABC, abstractmethod

# Abstract products
class CoffeeTable(ABC):
    def hasLegs():
        pass

class Chair(ABC):
    
    @abstractmethod
    def hasLegs():
        pass
    
    @abstractmethod
    def usedWith(self, table: CoffeeTable):
        pass

class Sofa(ABC):
    
    @abstractmethod
    def hasLegs():
        pass
    
    @abstractmethod
    def usedWith(self, table: CoffeeTable):
        pass

# Concrete Products
class ModernChair(Chair):

    def __init__(self) -> None:
        super().__init__()
    
    def hasLegs():
        return "has modern legs"
    
    def usedWith(self, table: CoffeeTable):
        # modern chair will only work with modern table. But it still takes any as argument
        print("Modern chair with Modern table")
        return 
    
class VictorianChair(Chair):

    def __init__(self) -> None:
        super().__init__()
    
    def hasLegs():
        return "has modern legs"
    
    def usedWith(self, table: CoffeeTable):
        print("victorian chair with victorian table")
        # victorian chair will only work with modern table. But it still takes any as argument
        return 
    
class ModernCoffeeTable(CoffeeTable):

    def __init__(self) -> None:
        super().__init__()
    
    def hasLegs():
        return "has modern legs"
    
class VictorianCoffeeTable(CoffeeTable):

    def __init__(self) -> None:
        super().__init__()

    def hasLegs():
        return "has victorian legs"

class ModernSofa(Sofa):

    def __init__(self) -> None:
        super().__init__()
    
    def hasLegs():
        return "has modern legs"
    
    def usedWith(table: CoffeeTable):
        print("modern chair with modern table")
        # modern Sofa will only work with modern table. But it still takes any as argument
        return 
    
class VictorianSofa(Sofa):

    def __init__(self) -> None:
        super().__init__()
    
    def hasLegs(self):
        return "has modern legs"
    
    def usedWith(table: CoffeeTable):
        # victorian Sofa will only work with modern table. But it still takes any as argument
        return 

class AbstractFactory(ABC):
    @abstractmethod
    def createChair(self) -> Chair:
        pass
    
    @abstractmethod
    def createTable(self) -> CoffeeTable:
        pass
    
    @abstractmethod
    def createSofa(self) -> Sofa:
        pass

# Concrete factories
class VictorianFactory(AbstractFactory):
    def createChair(self) -> Chair:
        print("You just created a victorian chair")
        return VictorianChair()

    def createTable(self) -> CoffeeTable:
        print("You just created a victorian table")
        return VictorianCoffeeTable()

    def createSofa(self) -> Sofa:
        print("You just created a victorian sofa")
        return VictorianSofa()

class ModernFactory(AbstractFactory):
    def createChair(self) -> Chair:
        print("You just created a modern chair")
        return ModernChair()

    def createTable(self) -> CoffeeTable:
        print("You just created a modern table")
        return ModernCoffeeTable()

    def createSofa(self) -> Sofa:
        print("You just created a modern table")
        return ModernSofa
    
def client_code(factory: AbstractFactory):
    chair = factory.createChair()
    table = factory.createTable()
    chair.usedWith(table)

client_code(VictorianFactory())
client_code(ModernFactory())






    


    
    



