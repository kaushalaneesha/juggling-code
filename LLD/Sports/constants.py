from enum import Enum

class Location:
    def __init__(self, ground, country) -> None:
        self.__ground = ground
        self.__country = country

class AccountStatus(Enum):
    ACTIVE, REGISTERED, ARCHIEVED, BLOCKED, UNKNOWN = 1, 2, 3, 4, 5

class GameStatus(Enum): 
    LIVE, OVER, CANCELLED = 1, 2, 3

class Result(Enum):
    WON, LOST, DRAW = 1, 2, 3

class GameType(Enum):
    ONE_DAY, TEST_MATCH, TWENTY_TWENTY = 1, 2, 3

class PlayerStatus(Enum): 
    PLAYING, OUT, BENTCH = 1, 2, 3

class PlayerType(Enum): 
    BOWLER, BATSMAN = 1, 2

class BallType(Enum): 
    NORMAL, WIDE, NO_BALL = 1, 2, 3

class WicketType(Enum): 
    CATCH, LBW = 1, 2