class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k, first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
                return

            for i in range(first, len(nums)):
                # Add nums[i] into the current combination
                curr.append(nums[i])

                # Use the next integers to complete the combination
                backtrack(k, i + 1, curr)

                # Backtrack
                curr.pop()


        output = []
        for k in range(len(nums)+1):
            backtrack(k)
        return output