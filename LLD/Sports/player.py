# Doubts: 
# Where should we keep result of the game? 

# Uniquely define the various game types. 
import datetime
from typing import List

from constants import BallType, GameStatus, GameType, Location, PlayerStatus, Result, WicketType

class Player:
    def __init__(self, name, number_of_matches: int, total_runs: int) -> None:
        self.__name = name
        self.__number_of_matches = number_of_matches
        self.__total_runs = total_runs
        # self.__matches = matches

class Team:
    def __init__(self, country, players: Player) -> None:
        self.__country = country
        self.__players = players
        self.__result = None
        self.__score = None         # Sum of scores of all the players of this team 

        def setResult(result: Result):
            self.__result = result

        def updateScore(score: int): # total score of the team
            self.__score = score

class PlayerInstance:
    def __init__(self, player: Player, runs: int) -> None:
        pass

class Wicket: 
    def __init__(self, bowler: PlayerInstance, wicket_type: WicketType, batsman: PlayerInstance, catch_by: PlayerInstance, run_out_by: PlayerInstance) -> None:
        self.__bowler = bowler
        self.__batsman = batsman
        self.__wicket_type = wicket_type 
        self.__catch_by = catch_by
        self.__run_out_by = run_out_by  

class Ball:
    def __init__(self, type: BallType, speed: float, bowler: PlayerInstance, batsman: PlayerInstance, runs: int, wicket: Wicket) -> None:
        self.__type = type
        self.__speed = speed
        self.__bowler = bowler
        self.__batsman = batsman
        self.__runs = runs
        self.__wicket = wicket
        

class Over: 
    def __init__(self, total: int, balls: List[Ball]) -> None:
        self.__total = total # number of balls
        self.__balls = balls





