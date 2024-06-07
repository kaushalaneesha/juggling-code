from behaviour import FlyWithWings, FlyNoWay, Quack

class Duck:
    def __init__(self) -> None:
        self._fly_behaviour = None
        self._quack_behaviour = None

    def perform_fly(self):
        self._fly_behaviour.fly()
    
    def perform_quack(self):
        self._quack_behaviour.quack()

    def swim(self):
        print("All ducks can swim!!")

    def set_fly_behaviour(self, fly_behaviour):
        self._fly_behaviour = fly_behaviour

class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        self._fly_behaviour = FlyWithWings()
        self._quack_behaviour = Quack()

class ModelDuck(Duck):
    def __init__(self) -> None:
        super().__init__()
        self._fly_behaviour = FlyNoWay()
        self._quack_behaviour = Quack()

# Device that mimcs Duck call: quack. 
class DuckCall:
    def __init__(self) -> None:
        self._quack_behaviour = None

    def perform_quack(self):
        self._quack_behaviour.quack()