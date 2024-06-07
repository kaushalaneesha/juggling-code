# Input to the function will be amount and portfolio object. return an object with the amount being equally distributed based on the portfolio given.

# stocks: AAPL, EA, ATVI, OKTA, TEAM
# portfolios: p1, ..., p4
# portfolios are defined as

#  * p1: 0.4 p2, 0.2 AAPL, 0.4 EA
#  * p2: 0.4 p3, 0.4 p4, 0.2 AAPL
#  * p3: 0.2 EA, 0.8 ATVI
#  * p4: 0.6 OKTA, 0.4 TEAM```
#  * 
# Portfolio can be nested  : ```p1: 0.4 p2, 0.2 AAPL, 0.4 EA ```
# Given the amount 1000$ and portfolio p4 as the input return as below
# ```/**
#  * e.g. Input given is p4, $1000 -> {"OKTA": $600, "TEAM": $400, ......}
#  * p1 ->  ??
#  * p2 ->  ??
#  * p3 -> ??
#  */```
# https://leetcode.com/discuss/interview-question/402902/Atlassian-or-Portfolios

class StockFraction:
    def __init__(self, stock, fraction) -> None:
        self.stock = stock 
        self.fraction = fraction

class Portfolio:
    def __init__(self) -> None:
        self.stock = None
        self.fraction = None
        self.portfolios = dict() #type Dict[Portfolio, Double]

    def add(self, stock, fraction):
        pp = Portfolio()
        pp.stock = stock
        pp.fraction = fraction
        self.addPortfolio(pp, 1.0)

    def addPortfolio(self, portfolio, fraction):
        self.portfolios[portfolio] = fraction
    
    def getStockFraction(self):
        if not self.isStockFraction:
            raise Exception("No stock fraction")
        return StockFraction(self.stock, self.fraction)
    
    def isStockFraction(self):
        return self.stock and self.fraction
    
    def getPortfolios(self):
        return self.portfolios
    

def splits(amount: float, portfolio: Portfolio) -> dict():
    map = dict()
    for pp, fraction in portfolio.getPortfolios().items():
        if pp.isStockFraction():
            # add the stock fraction directly to map
            map[pp.stock] = map.get(pp.stock, 0.0) + pp.fraction * amount
        else:
            # if its a portfolio
            mPrev = splits(amount * fraction, pp)
            for stock, am in mPrev.items():
                map[stock] = map.get(stock, 0) + am
    return map

p4 = Portfolio()
p4.add("OKTA", 0.6)
p4.add("TEAM", 0.4)

p3 = Portfolio()
p3.add("EA", 0.2)
p3.add("ATVI", 0.8)

p2 = Portfolio()
p2.addPortfolio(p3, 0.4)
p2.addPortfolio(p4, 0.4)
p2.add("APPL", 0.4)

p1 = Portfolio()
p1.addPortfolio(p2, 0.4)
p1.add("APPL", 0.2)
p1.add("EA", 0.4)

print(splits(1000, p4))
print(splits(1000, p3))
print(splits(1000, p2))
print(splits(1000, p1))


        
