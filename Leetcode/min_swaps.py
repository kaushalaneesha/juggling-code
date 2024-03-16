# Function returns the 
# minimum number of swaps 
# required to sort the array 
from functools import cmp_to_key 
  
  
def cmp(a, b): 
    return b - a
  
  
def minSwaps(nums): 
    Len = len(nums) 
    map = {} 
    for i in range(Len): 
        map[nums[i]] = i 
  
    nums = sorted(nums, key=cmp_to_key(cmp)) 
  
    # To keep track of visited elements. Initialize 
    # all elements as not visited or false. 
    visited = [False for col in range(Len)] 
  
    # Initialize result 
    ans = 0
    for i in range(Len): 
  
        # already swapped and corrected or 
        # already present at correct pos 
        if (visited[i] or map[nums[i]] == i): 
            continue
  
        j, cycle_size = i, 0
        while (visited[j] == False): 
            visited[j] = True
  
            # move to next node 
            j = map[nums[j]] 
            cycle_size += 1
  
        # Update answer by adding current cycle. 
        if (cycle_size > 0): 
            ans += (cycle_size - 1) 
  
    return ans 

print(minSwaps([2, 8, 4, 0, 8, 9, 2]))