
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        # Approach: Find the steps needed for A and B respectively. Take the max
        steps = 0
        if len(A) == 1:
            return 0 
        for i in range(1, len(A)):
            steps += abs(max(abs(A[i] - A[i-1]), abs(B[i] - B[i-1])))
            print(steps)
            
        return steps
            
A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
s = Solution()
print(s.coverPoints(A, B))
