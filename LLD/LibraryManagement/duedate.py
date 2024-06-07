import datetime
from order import Order

class DueDateManager:
    def isPastDueDate(order: Order) -> bool:
        # order._date - datetime.now() > 10
        return True
    
    