class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        total = A[-1]

        i = len(A)-2

        

        if i==0:

            return sum(A)

        elif i==1:

            return A[-1]

            

        while i > 0:

            if A[i]>=A[i-1]:

                total += A[i-1]
                print(i)
                i -= 2
                print(i)

            elif A[i]<A[i-1]:

                total += A[i]
                print(i)
                i -= 1
                print(i)
        

        return total

s = Solution()
print(s.solve([4, 1, 2, 1, 3]))