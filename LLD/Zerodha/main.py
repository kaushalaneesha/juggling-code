from constants import *
from stock import Stock
from user import User
from order import *


user = User("12", "Aneesha")
stock = Stock("TCS", 1000, ExchangeType.NSE)
order = Order(TransactionType.BUY, OrderType.MARKET, ExchangeType.NSE, stock, 2, 1000)
orderManager = OrderManager()
orderManager.place_order(order, "12")
