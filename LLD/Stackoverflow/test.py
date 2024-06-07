from account_type import Member
from entity import Question


question = Question(["python", "java"])
question.__content = "What a question"
user = Member()
user.getQuestions()