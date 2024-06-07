from abc import ABC
class GoalStatus(Enum):
    NOT_MET, NEAR_COMPLETE, FAR_AWAY, MET = 1, 2, 3, 4
class Rewards:
    def __init__(self) -> None:
        self._rewards = None

class Goal:
    def __init__(self, name, goal) -> None:
        self._goal_value = goal
        self._goal_name = name
        self._status = GoalStatus.NOT_MET
        self._rewards = None

    def is_near_done(self, curr_value):
        if curr_value >= self._goal_value * .80:
            self._status = GoalStatus.NOT_MET
            # some notifcation
            return True
        
    def is_far_behind(self, curr_value):
        if curr_value >= self._goal_value * .20:
            self._status = GoalStatus.FAR_AWAY
            # some notification
            return True
        
    def goal_met(self):
        self._rewards += 100


class FitnessMetrics(ABC):
    def __init__(self, metrics_type) -> None:
        self._curr_value = 0
        self._goal = None
        self._metrics_type = metrics_type
        
    # will come from external system
    def set_metrics(self, curr_value):
        self._curr_value = curr_value

    def reset_metrics(self):
        self._curr_value = 0

    def set_goal(self, goal: Goal):
        self._goal = goal

   

class WaterFitnessMetrics(FitnessMetrics):
    def __init__(self) -> None:
        super().__init__("water")
    
    def is_near_done(self):
        if self._curr_value >= self._goal_value * .70:
            # notify user
            return True

class CalorieFitnessMetrics(FitnessMetrics):
    def __init__(self) -> None:
        super().__init__("calories")

class WorkoutFitnessMetrics(FitnessMetrics):
    def __init__(self) -> None:
        super().__init__("workout")      

class StepsFitnessMetrics(FitnessMetrics):
    def __init__(self) -> None:
        super().__init__("steps")     
     
class User:
    def __init__(self) -> None:
        self._id = id
        self._metrics = []
        self._rewards = 0

class Analytics(ABC):
    def __init__(self) -> None:
        metrics_history = None # <user_id, >

class WeeklyAnalytics(Analytics):
    pass

class MonthlyAnalytics(Analytics):
    pass

# class NotificationSystem(ABC):
#     def __init__(self) -> None:
#         self._observers = []

#     def addObserver(self, user: User):
#         self._observers.append(user)

#     def notify(self): pass

# class MobileNotification(NotificationSystem):
#     def __init__(self) -> None:
#         self._observers = []

#     def addObserver(self, user: User):
#         self._observers.append(user)

#     def notify(self): 
#         for observer in self._observers:
    



