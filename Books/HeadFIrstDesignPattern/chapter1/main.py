from behaviour import FlyWithRocket
from duck import MallardDuck, ModelDuck

duck = MallardDuck()
duck.perform_fly()
duck.perform_quack()

duck2 = ModelDuck()
duck2.perform_fly()
duck2.set_fly_behaviour(FlyWithRocket())
duck2.perform_fly()