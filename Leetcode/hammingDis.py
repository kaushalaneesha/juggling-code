import collections
# class Solution:
# 	# @param A : tuple of integers
# 	# @return an integer
#     def hammingDistance(self, A):
#         def count_bits(n):
#             count = 0
#             while n:
#                 n &= n-1
#                 count += 1
#             return count
        
#         count_bits_map = collections.defaultdict(int)
#         n = len(A)
#         if n == 1:
#             return 0
#         dis = 0
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if A[i] != A[j]:
#                     if not count_bits_map[(A[i], A[j])]:
#                         xor = A[i] ^ A[j]
#                         cxor = count_bits(xor)
#                         count_bits_map[(A[i], A[j])] = cxor
#                         count_bits_map[(A[j], A[i])] = cxor
#                     dis += 2 * count_bits_map[(A[i], A[j])]
#         return dis

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def hammingDistance(self, A):
        i = 0
        dis = 0
        for i in range(32):  # for every position starting from last count the number of 0s and number of 1s
            count_zeros = count_ones = 0
            for num in A:
                bit_val = num & 1 << i
                if bit_val == 0:
                    count_zeros += 1
                else:
                    count_ones += 1
            dis += 2 * count_ones * count_zeros
        return dis
        
    
s = Solution()
print(s.hammingDistance([2, 4, 6]))