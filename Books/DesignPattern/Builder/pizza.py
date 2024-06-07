from abc import ABC, abstractmethod
from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3                  # in seconds for the sake of the example

class Pizza:
    def __init__(self, name) -> None:
        self.__name = name
        self.__dough = None
        self.__topping = []
        self.__sauce = None

    def __str__(self) -> str:
        return self.__name
    
    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))

class PizzaBuilder(ABC):
    @abstractmethod
    def add_topping(self):
        pass
    
    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def prepare_dough(self):
        pass

class MargaritaPizzaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.__pizza = Pizza("Margarita")
        self.progress = PizzaProgress.queued

    def add_topping(self):
        print("Add margarita topping: mozzarella")
        self.__pizza.__topping = [PizzaTopping.mozzarella]
    
    def add_sauce(self):
        print("Add margarita sauce")
        self.__pizza.__sauce = PizzaSauce.tomato

    def bake(self):
        self.progress = PizzaProgress.baking
        print("Baking Margarita Pizza")

    def get_pizza(self):
        self.progress = PizzaProgress.ready
        print("Here is your margarita pizza!!")
        return self.__pizza
    
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.__pizza.prepare_dough(PizzaDough.thin)

class CreamyBaconPizzaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.__pizza = Pizza("Creamy Bacon")
        self.progress = PizzaProgress.queued

    def add_topping(self):
        print("Add creamy bacon topping")
        self.__pizza.__topping = [PizzaTopping.bacon, PizzaTopping.ham]
    
    def add_sauce(self):
        print("Add creamy bacon sauce")
        self.__pizza.__sauce = PizzaSauce.creme_fraiche

    def bake(self):
        self.progress = PizzaProgress.baking
        print("Baking creamy bacon Pizza")

    def get_pizza(self):
        self.progress = PizzaProgress.ready
        print("Here is your creamy pizza!!")
        return self.__pizza
    
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.__pizza.prepare_dough(PizzaDough.thick)
    
class Chef:
    # The director class
    def __init__(self) -> None:
        self.__builder = None

    def make_pizza(self, pizzaBuidler: PizzaBuilder):
        self.__builder = pizzaBuidler
        pizzaBuidler.prepare_dough()
        pizzaBuidler.add_sauce()
        pizzaBuidler.add_topping()
        pizzaBuidler.bake()

    def get_pizza(self):
        self.__builder.get_pizza()


marg_builder = MargaritaPizzaBuilder()
bacon_builder = CreamyBaconPizzaBuilder()
chef = Chef()

chef.make_pizza(marg_builder)
chef.get_pizza()
chef.make_pizza(bacon_builder)
chef.get_pizza





