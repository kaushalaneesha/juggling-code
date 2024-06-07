class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Brute force check if subarray of each length is a permutation
        def isPermutation(arr) -> bool: 
            for i, num in enumerate(sorted(arr)): 
                if i+1 != num:
                    return False
            # print(True)
            return True
        
        res = 0
        N = len(A)
        for i in range(1, N + 1): # length of subarray we are considering
            for j in range(N):    # start of subarray
            #    print(i + j)
            #    print(A[j:(j + i)])

               if i + j <= N and isPermutation(A[j:(j + i)]):
                   res += 1
    
        return res
    
    
S = Solution()
print(S.solve([2, 1, 3, 4]))