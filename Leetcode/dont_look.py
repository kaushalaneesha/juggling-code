class Solution:
    # @param A : string
    # @return an integer
    def turnPigeons(self, A):
        # count = 0
        # Ls = A.count('L')
        # Rs = A.count('R')
        # print(Ls)
        # print(Rs)
        # new_char = 'L' if Ls > Rs else 'R'
        # index = A.find("RL")
        # while index != -1:
        #     if new_char == 'R':
        #         index += 1
        #     A = A[:index] + new_char + A[index+1:]
        #     count += 1
        #     index = A.find("RL")
        # print(A)
        # return count 
    
        n = len(A)
        pref = [0] * (n+2)
        suff = [0] * (n+2)

        # Count number of Rs in first half
        for i in range(1, n+1):
            pref[i] = pref[i-1]
            if A[i-1] == 'R':
                pref[i] += 1
            
        for i in range(n, 0, -1):
            suff[i] = suff[i+1]
            if A[i-1] == 'L':
                suff[i] += 1
        
        ans = 1000000
        breakpoint = 0
        for i in range(0, n + 1):
            if pref[i] + suff[i+1] <  ans:
                ans = pref[i] + suff[i+1]
                breakpoint = i
        # print(breakpoint)
        return ans

ss = 'RLLLLLRLLRLLLLRRRRRRLLRLRLLRLLRLLLLLRLLRLLLRLRRLRRLLLLRLLRRRLLLLLRLLLLLRLLLRRRLLRRRRLLLLRR'
s = Solution()
print(s.turnPigeons(ss))
# print(ss[:75])
# print(ss[:75].count('R'))
# print()
# print(ss[75:])
# print(ss[75:].count('L'))
