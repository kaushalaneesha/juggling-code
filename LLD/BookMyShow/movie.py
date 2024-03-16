# Class for Movie and shows

import datetime

from LLD.BookMyShow.BMSService import CinemaHall


class Movie:

    def __init__(self, name, id, duration, languages, genre, release_date):
        self.__name = name
        self.__id = id
        self.__duration = duration
        self.__language = languages # list of languages
        self.__genre = genre    # list of genres 
        self.__release_date = release_date

        self.__shows = []

    def get_shows(self):
        pass    

class Show:

    def __init__(self, id: str, movie: Movie, start_time: datetime, end_time: datetime):
        self.__id = id
        self.__movie = movie
        self.__start_time = start_time
        self.__end_time = end_time

        self.__played_at = None
        self.__seats = []

