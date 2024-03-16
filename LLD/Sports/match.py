            
from ast import List
import datetime

from constants import GameStatus, GameType, Location, WicketType
from player import Over, PlayerInstance, Team


class Innings:
    def __init__(self, players: List[PlayerInstance], id: str, wickets: List[WicketType], overs: List[Over]) -> None:
        self.__player_instance = players
        self.__id = id
        self.__wickets = wickets
        self.__overs = overs

class Match:
    def __init__(self, id, type: GameType, played_on, start_time: datetime, end_time: datetime, location: Location, team_a: Team, 
                 team_b: Team, status: GameStatus, innings: List[Innings]) -> None:
        self.id = id
        self.type = type
        self.played_on = played_on
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.team_a = team_a
        self.team_b = team_b
        self.innings = innings 
        self.__game_status = status