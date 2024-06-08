"""
    Brute force approach
    1. Iterate over the array lets say with pointer i
        1.1 Take another point j, starting at i+1. Increment it till sum(nums[i,j+1]) is
            multiple of k. Rreturn true if such sum is found
    2. Return false if no such number is found

    Complexity
    Time: O(n2): This one gives time exceeded exception
    Space: O(1)

    Appoarch 2: Prefix sum and hashing. (had to consult leetcode editorial)
    To find: We want a subarray with sum divisible by k i.e.
    ( prefix[j] - prefix[i] ) % k == 0 ----------------------- (1)

    Lets say
    prefix[j] = Q1 * k + R1
    prefix[i] = Q2 * k + R2

    Putting these values in first equation
    (Q1 * k + R1 - (Q2 * k + R2)) % k == 0
    
    k * (Q1-Q2) will be divisible by k
    that means in about R1 - R2 should also be divisible by k

    R1 and R2 lie in range [0,k) 
    So they can only be divisible by k if R1 - R2 == 0 
    So we should have R1 == R2  --------------- (2)

    Putting R1 = prefix[j] % k and R2 = prefix[i] % k in 2
    prefix[j] % k = prefix[i] % k

    [0 5 1 5 5 0] 
    [0 5 1 5 5 0]

    Algorithm
    2. Iterate over the array and using the formula preMod = ( preMod + nums[i] ) % k
        compute the current prefix mod, lets call it preMod
    3. Keep puting the preMod in a hashmap, with key as preMod and value as index
    4. If the same value of preMod comes again check if the length of subarray is greater than 
       1(diff between values). If yes return true. Else complete it for the whole array
    5. Return false if no such array is found

"""
from typing import List


class Solution:
    # Brute Force 
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     n = len(nums)
    #     for i in range(n):
    #         _sum = nums[i]
    #         for j in range(i+1, n):
    #             _sum += nums[j]
    #             if _sum % k == 0:
    #                 return True
    #     return False

    # Prefix and Hashmap
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preMod = 0
        mods = {0: -1}
        for i, num in enumerate(nums):
            preMod = ( preMod + num ) % k 
            if preMod in mods:
                if i - mods[preMod] > 1:
                    return True
            else:
                mods[preMod] = i
        return False


s = Solution()
print(s.checkSubarraySum([23,2,4,6,7], 6)) # Expected True
print(s.checkSubarraySum([23,2,6,4,7], 6)) # Expected True
print(s.checkSubarraySum([23,2,6,4,7], 13)) # Expected False

