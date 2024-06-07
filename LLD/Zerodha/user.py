class User:
    def __init__(self, id, name) -> None:
        self._id = id 
        self._name = name
        self._funds = None 
        self._portfolio = None
        self._watchlist = None

# Keeping everything as static
class UserCatalog:
    users = {} # Map of user id to User

    def add_user(user: User): 
        UserCatalog.users[user._id] = user

    def get_user(userId: str) -> User: 
        return UserCatalog.users.get(userId)

