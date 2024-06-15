from typing import List

# Find the avg from the list. 
def average(input: List[int]):
    if not input:
        return 0
    summ = sum(input)
    total = len(input)
    return summ / total

# List contains item prices and there will be budgest find how many items  can you buy? --Test cases passed
# Prices [ 10.0 , 5.0 , 20.0] Budget 35
def max_items(prices: float, budget: int) -> int:
    prices.sort()
    res = 0
    curr_items = 0
    for price in prices:
        if price > budget:
            break
        curr_items = budget // int(price)
        print(curr_items)
        budget = budget % price
        res += curr_items
    return int(res)

print(max_items([10.0, 5.5, 20.0], 35.0))







