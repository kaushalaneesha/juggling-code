class Solution:
    # def palindromicPartition(self, string):
    #     def helper(string, start, end):
    #         ans = 1000
    #         if start >= end:
    #             return 0
    #         if "".join(reversed(string[start:end])) == string[start:end]:
    #             return 0
    #         for k in range(start+1, end):
    #             temp = helper(string, start, k) + helper(string, k, end) + 1
    #             if ans > temp:
    #                 ans = temp
    #         return ans
    #     return helper(string, 0, len(string))
    
    def palindromicPartition(self, string):
        cuts = [[-1 for i in range(len(string))] for j in range(len(string))]
        def helper(string, start, end):
            ans = 1000
            if start >= end:
                return 0
            if "".join(reversed(string[start:end])) == string[start:end]:
                return 0
            if cuts[start][end-1] != -1:
                return cuts[start][end-1]
            for k in range(start+1, end):
                temp = helper(string, start, k) + helper(string, k, end) + 1
                if ans > temp:
                    ans = temp
            cuts[start][end-1] = ans
            print(ans)
            return ans
        helper(string, 0, len(string))
        print(cuts)
        return helper(string, 0, len(string))
    
    def minCut(self, s: str) -> int:
        n=len(s)
        t=[[-1 for i in range(2001)]for j in range(2001)]
        def isPalindrome(st):
            return st==st[::-1]
        def solve(s,i,j):
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            if isPalindrome(s[i:j+1]):
                return 0
            ans = float("inf")
            for k in range(i,j):
                if isPalindrome(s[i:k+1]):
                    temp_ans = solve(s,k+1,j)+1
                    ans=min(ans,temp_ans)
            t[i][j]= ans
            return ans
        i,j = 0,n-1
        return solve(s,i,j)







    def minCut(self, s: str) -> int:
        minCuts = [[-1 for i in range(len(s))] for j in range(len(s))]
        return self.palindromePartitionHelper(s, 0, len(s), minCuts)
            
    def palindromePartitionHelper(self, string, start, end, minCuts):
        if start >= end:
            return 0
        substr = string[start:end]
        if minCuts[start][end-1] != -1:
            return minCuts[start][end-1]
        if substr[::-1] == substr:
            minCuts[start][end-1] = 0
            return 0
        minCutForSubStr = len(substr)-1
        for i in range(start+1, end):
            leftSubstrCuts = self.palindromePartitionHelper(string, start, i, minCuts)
            rightSubstrCuts = self.palindromePartitionHelper(string, i, end, minCuts)
            if (minCutForSubStr > leftSubstrCuts + rightSubstrCuts + 1):
                minCutForSubStr = leftSubstrCuts + rightSubstrCuts + 1
        minCuts[start][end-1] = minCutForSubStr
        return minCutForSubStr

#     a a b b b a
#   a
#   a
#   b
#   b
#   b
#   a  


sol = Solution()
print(sol.palindromicPartition("ababbbabbababa"))