class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        return self.lcs_helper(x, y, s1, s2, 0)
    
    def lcs_helper(self, x, y, s1, s2, count):
        if x <= 0 or y <= 0:
            return 0
        if s1[x-1] == s2[y-1]:
            return self.lcs_helper(x-1, y-1, s1[:x-1], s2[:y-1], count + 1)
        else:
            return max(count, self.lcs_helper(x-1, y, s1[:x-1], s2[:y], count), self.lcs_helper(x, y-1, s1[:x], s2[:y-1], count))
           
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
