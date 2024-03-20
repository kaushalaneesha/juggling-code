from abc import ABC
import datetime
from typing import List

class Comment:
    def __init__(self, posted_by, posted_on, content) -> None:
        self.__posted_by = posted_by
        self.__posted_on = posted_on
        self.__content = content 
        self.__upvotes = None

    

class Entity(ABC): 
    def __init__(self, id: str, content: str, posted_by, posted_on: datetime) -> None:
        self.id = str
        self.__content = content
        self.__posted_by = posted_by
        self.__posted_on = posted_on
        self.__comments = []

        self.up_votes = set() # Unique list of members ids who have up voted
        self.down_votes = set() # Unique list of member ids who have down voted

        # def upVote(member: Member):
        #     self.up_votes.add(member.id)

        # def downVote(member: Member):
        #     self.down_votes.add(member.id)

        # def total_upvotes():
        #     return len(self.up_votes)
        
        # def total_downvotes():
        #     return len(self.down_votes)
        

        
class Question(Entity):
    def __init__(self, tags) -> None:
        self.__tags: tags
        self.__is_duplicate = False
        self.__comments = None

class Answer(Entity):
    def __init__(self, tags) -> None:
        self.__is_accepted = False
        self.__comments = None
