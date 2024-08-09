from typing import List

[1,2,3,4,5]
def sum_closest(nums: List[int], target: int) -> int:
    # iterate through the list and use 2 pointers
    i = 0
    j = len(nums) - 1
    
    curr_sum = 0
    while i < j:
        print(i,j)
        if nums[i] + nums[j] == target:
            return [nums[i],nums[j]]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            pair = [nums[i], nums[j]]
            i += 1
    return pair

print(sum_closest([1,2,3,4,5], 10))

