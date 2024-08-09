from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  cells = R * C
  battleships = 0
  for r in range(R):
    for c in range(C):
      if G[r][c] == 1:
        battleships += 1
  return round(battleships / cells, 6) 
  
# G = [[0, 0, 1],
#     [1, 0, 1]]
# print(getHitProbability(2, 3, G))
# G = [[1, 1], [1, 1]]
# print(getHitProbability(2, 2, G))

from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  def neighbourDiner(i: int): 
    for j in range(K+1):
      if i + j <= N and i + j in seats:
        return True
      if i - j > 0 and i - j in seats:
        return True
    return False
      
  seats = set(S)
  res = 0
  for i in range(1, N + 1):
    if not neighbourDiner(i):
      res += 1
      for j in range(K):
        if i + j <= N:
          seats.add(i + j)
        if i - j > 0 and i - j in seats:
          seats.add(i - j)
  return res

print(getMaxAdditionalDinersCount(10, 1, 2, [2,6]))
print(getMaxAdditionalDinersCount(15, 2, 3, [11, 6, 14]))