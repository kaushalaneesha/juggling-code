# Doubts: 
# Should price be associated with game type instead. In subscrption we can just calculate it based on game type and number of days

from datetime import datetime

from LLD.Sports.game import Game


# Each subscritpion should have some notifcation preference associated with it. 

class Subscription:
    def __init__(self, id, start_date: datetime, end_date: datetime, notfication: Notification, game: Game, price: float) -> None:
        self.__id = id
        self.__start_date = start_date
        self.__end_date = end_date
        self._game = game
        self._notification_preference = notfication