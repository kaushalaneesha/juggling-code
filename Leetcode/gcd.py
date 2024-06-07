def gcd(x, y): 
    if x > y:
        x, y = y, x    # Make y the greater element
    while x:
        x, y = y % x, x
    return y
        
class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        num2 = pow(10, B)
        return gcd(int(A), num2)

s = Solution()
print(s.solve("12345", 2)) # expected 5