import sys
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        curr_sum = 0
        max_sum = -1 * sys.maxsize
        curr_start_index = -1
        curr_end_index = -1
        max_start_index = -1
        max_end_index = -1
        for i, num in enumerate(A):
            if num >= 0:
                curr_sum += num
                curr_end_index = i
                if curr_start_index == -1:
                    curr_start_index = i
            if num < 0 or i == len(A) - 1: # break the current sum
                if max_sum < curr_sum or (max_sum == curr_sum and max_start_index == -1):
                    max_sum = curr_sum
                    max_start_index = curr_start_index
                    max_end_index = curr_end_index
                curr_sum = 0
                curr_start_index = -1

        return A[max_start_index:max_end_index+1]
                    
                
s = Solution()
print(s.maxset([0, 0, -1, 0]))
print(s.maxset([1, 2, 5, -7, 2, 3]))
print(s.maxset([10, -1, 2, 3, -4, 100]))
print(s.maxset([-1, -1, -1, -1]))
print(s.maxset([-4, 0, -4]))
