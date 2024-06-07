from enum import Enum


class TransactionType(Enum):
    BUY, SELL = 1, 2

class OrderType(Enum):
    MARKET, LIMIT = 1, 2 

class ExchangeType(Enum):
    NSE, BSE = 1, 2

class OrderStatus:
    OPEN, CANCELLED = 1, 2