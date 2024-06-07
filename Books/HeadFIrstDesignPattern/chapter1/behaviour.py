from abc import ABC

class FlyBehaviour(ABC):
    def fly(self):
        pass

class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("This duck flies with wings")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("This duck doesn't fly")

class FlyWithRocket(FlyBehaviour):
    def fly(self):
        print("Flying with a rocket!")

class QuackBehaviour(ABC):
    def quack(self):
        pass

class Quack(QuackBehaviour):
    def quack(self):
        print("quack!")

class SqueakQuack(QuackBehaviour):
    def quack(self):
        print("squeak!")
    
class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< silence >>")