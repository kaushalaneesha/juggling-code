"""
Intuition:
This question is pretty similar to https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-06-08
So we can use the same apporach of prefix and hashes, that is for a subarray of i+1 to j to be divisible by 
k it should have prefixMod[i] = prefixMod[j]
To understand the maths behind it refer to: https://github.com/kaushalaneesha/juggling-code/blob/main/Leetcode/523_continuous_subarray_sum.py

Basically computing the prefix modules at each index, using formula:
prefixMod[i] = ( prefixMod[i-1] + num[i] ) % k
For first example it will be, note length of prefixMod is n + 1, at zeroth index we just have 0:
[0, 4, 4, 4, 2, 4, 0]

Logic to add here is to count how many pairs (combinations) are there which has same prefix modulus, by formula
0 comes twice so it will be = 1 pair
4 comes 3 times so it will be (4*3)/2 = 6 pairs

Total pairs = 7

Approach: 
1. Compute the prefixMod by above logic. 
2. Keep saving the prefixMod and their number of occurence in a map. 
3. Iterate over the keys of the map. And apply nC2 on each value and add it to result. 
4. Return result. 

Complexity:
Time = O(n)
Space = O(n)
"""

import collections
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Fill the prefix array
        prefix_mod = [0] * (n+1)
        mod_seen = collections.defaultdict(int)
        mod_seen[0] = 1
        for i, num in enumerate(nums):
            prefix_mod[i+1] = (prefix_mod[i] + num) % k
            mod_seen[prefix_mod[i+1]] += 1

        result = 0
        for k, v in mod_seen.items():
            if v > 1:
                result += (v * (v - 1)) // 2 
        return result
        
s = Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1], 5)) # Expected 7
print(s.subarraysDivByK([5], 9)) # Expected 0
