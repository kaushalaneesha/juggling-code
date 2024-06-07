import math
def allFactors(A):
    upperLimit = A ** 0.5
    upperLimitInt = int(upperLimit)
    factors = [i for i in range(1, upperLimitInt+1) if A % i == 0]
    factors.extend([A // i for i in factors if i != upperLimit])
    return sorted(factors)

print(allFactors(38808))