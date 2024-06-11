from typing import List


class Solution:
    """
    Intiution : 
    
    First thought
    - Iterate over arr1 and keep the count of each element in a map. count_map
    - Iterate over arr2. Keep storing each element as it has come number of times 
    in the above map(count_map). 
    - For the remaining elements in the map, we would need to do some sorting and
    add them as well. 

    Can I do some improvement for the step 3? Sorting of remaining elements. 

    If we check the constraints we can see that the value of elements are of the range 0 
    to 1000. So rather than creating a map we can have an array and we can keep count of all
    elements from arr1. 

    In step 3, we can iterate over those 1000 indexes and since array is already sorted add them to the
    result list. 

    Approach: 
    1. Create a count_list of size 1001. Create a result list of size arr1
    2. Iterate over arr1 and update the count in count_list. 
    3. Iterate over arr2, for each element add it to result list as its value in count_list. 
       Update the count in arr1 to 0. 
    4. Iterate over count_list, for the elements still having count > 0. Add them to the result list. 

    Complexity: 
    Time: O(1000 + n) => O(n)
    Space: O(n) => count_list and result
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_list, result = [0]*1001, []
        for elem in arr1:
            count_list[elem] += 1
        for elem in arr2:
            result += ([elem] * count_list[elem])
            count_list[elem] = 0
        for i in range(1001):
            if count_list[i] > 0:
                result += ([i] * count_list[i])
                count_list[i] = 0
        return result
        
s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))