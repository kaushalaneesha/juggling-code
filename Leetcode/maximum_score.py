# https://www.youtube.com/watch?v=RRQVDqp5RSE\

# Time Complexity: O(n ^ 2 * 2^n * logm)
import math
import collections
class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        cache = collections.defaultdict(int) # Store the gcd for a subproblem. 
                   # Key will be the bitmask idicating what keys are already selected and which are left
                   # 2 ^ n numbers where n = 2 * A  
        gcd = [[0 for i in range(len(B))] for j in range(len(B))]
        def computeGCD(x, y): 
            while y: 
                x, y = y, x % y
            return x
        
        def dfs(mask, operation):
            if mask in cache: 
                return cache.get(mask) 
            # calculate the score for all possible combination of 2 numbers 
            for i in range(len(B)):
                if (1 << i) & mask:
                    continue 
                for j in range(i + 1, len(B)):
                    # check if i and j are already selected in the mask
                    if (1 << j) & mask:
                        continue
                    # since we are selecting i and j. Mark them as 1 in the mask ( using OR )
                    newMask = mask | (1 << i) | (1 << j)
                    score = operation * gcd[i][j]
                    cache[mask] = max(cache[mask], score + dfs(newMask, operation + 1)) 
            return cache[mask]
        
        #Compute gcd of all possible values
        for i in range(len(B)):
            for j in range (i + 1, len(B)):
                gcd[i][j] = computeGCD(B[i], B[j]) 
        return dfs(0, 1)
            
A = 3
B = [3, 4, 9, 5]
B = [8, 5, 6, 25, 6, 16]
s = Solution()
print(s.solve(A, B))