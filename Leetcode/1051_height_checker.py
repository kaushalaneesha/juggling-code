from typing import List


class Solution:
    """
        Clone the array into sorted list
        Iterate both the lists together. 
        Count the number of instances where you dont see a match
    """
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        non_matching_heights = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                non_matching_heights += 1
        return non_matching_heights 
        
s = Solution()
print(s.heightChecker([1,1,4,2,1,3])) # 3
print(s.heightChecker([5,1,2,3,4])) # 5
print(s.heightChecker([1,2,3,4,5])) # 0