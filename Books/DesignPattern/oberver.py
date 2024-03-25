from abc import ABC


class Subscriber(ABC):
    def notify(self):
        pass

class User(Subscriber):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def notify(self, message):
        print("The user {} received a message: {}".format(self.name, message))

class Group:
    def __init__(self) -> None:
        self.subscribers = []
    
    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for sub in self.subscribers:
            sub.notify(message)
    
grp = Group()
user1 = User(1)
grp.subscribe(user1)
grp.subscribe(User(2))
grp.subscribe(User(3))

grp.notify("new message")
grp.unsubscribe(user1)
grp.notify("another message")
