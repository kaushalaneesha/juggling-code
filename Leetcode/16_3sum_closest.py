class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i = 0
        j = i + 1
        k = len(nums) - 1
        curr_sum = sum(nums[0:3])
        nums.sort()
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ < target:
                    j += 1
                elif summ > target:
                    k -= 1
                else:
                    return summ
                if abs(target - summ) < abs(curr_sum - target):
                    curr_sum = summ
        return curr_sum
