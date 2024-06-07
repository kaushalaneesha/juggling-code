
def jump(nums, start, jumps) -> int:
    if start > len(nums):
        return jumps
    val = nums[start]
    minJumps = 100000
    print(nums[start])
    for i in range(1, val+1):
        currJumps = jump(nums, i+start, jumps + 1)
        if minJumps > currJumps:
            minJumps = currJumps
    return minJumps

jump([2,3,1,1,4], 0, 0)