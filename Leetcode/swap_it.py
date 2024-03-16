class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Problem can be translated into number of swaps needed to sort the array in decending order
        # i = 0
        # count_swaps = 0
        # n = len(A)
        # if B >= n * n:
        #     return 1
        # while i < len(A):
        #     max_index = A[i:].index(max(A[i:])) + i
        #     # print(i)
        #     # print(max_index)
        #     if max_index != i and A[i] < A[max_index]:
        #         # swap the elements
        #         A[i], A[max_index] = A[max_index], A[i] 
        #         count_swaps += (max_index - i)
        #         print(count_swaps)
        #     i += 1
        # print("count swaps: {}".format(count_swaps))
        # return 1 if B >= count_swaps else 0

        cnt = 0
        for dig in range(9, -1, -1): 
            temp = []
            ind = 0
            for i in range(len(A)):
                if A[i] == dig:
                    cnt += (i - ind)
                    ind += 1
                else: 
                    temp.append(A[i])
            A = temp
            print(A)
            print(cnt)
        print(cnt)
        return 1 if B >= cnt else 0

A = [2, 8, 4, 0, 8, 9, 2]
B = 1   
s = Solution()
print(s.solve(A, B))