from sortedcontainers import SortedList, SortedSet, SortedDict 
import bisect
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        res = []
        #-------------------BRUTE FORCE------------------------------
        # for i, num in enumerate(A):
        #     sr, sl, ll, lr = 0, 0, 0, 0

        #     # Find small & large numbers before ith index
        #     for j in range(i):
        #         if A[j] < num:
        #             sl += 1
        #         else:
        #             ll += 1
        #     for j in range(i+1, n):
        #         if A[j] < num:
        #             sr += 1
        #         else:
        #             lr += 1
            
        #     # check if ith index is magic: 
        #     if sl * sr - lr * ll >= 0:
        #         res.append(1)
        #     else:
        #         res.append(-1)
        # return res
        
        #------------------SORTED LIST----------------------------------
        # s = SortedList()
        # sl = [] # smaller elements at left
        # for num in A:
        #     index=bisect.bisect_left(s, num)
        #     sl.append(index)
        #     s.add(num)
            
        # print(sl)
        # s = SortedList()
        # sr = [] # smaller elements at right
        # for num in A[::-1]:
        #     index=bisect.bisect_right(s, num)
        #     sr.append(index)
        #     s.add(num)
        # sr = sr[::-1]
        # print(sr)
        
        # for i in range(len(A)): 
        #     # check if ith index is magic: 
        #     if sl[i] * sr[i] - (i - sl[i]) * (n-1-i-sr[i]) >= 0:
        #         res.append(1)
        #     else:
        #         res.append(-1)

        # return res
    
        #-----------------MERGE SORT----------------------------------------
        
        sr = smallRight(A, n)
        sl = smallRight(A[::-1], n)[::-1]
        print(sl)
        print(sr)
        for i in range(len(A)): 
            # check if ith index is magic: 
            if sl[i] * sr[i] - (i - sl[i]) * (n-1-i-sr[i]) >= 0:
                res.append(1)
            else:
                res.append(-1)
        
        return res


def smallRight(A, n):
    s = []
    ind = [i for i in range(n)]
    count = [0]*n
    mergeSort(A, 0, n - 1, count, ind)
    return count

def mergeSort(arr, left, right, count, ind): 
    # arr: Array to be sorted
    # start of array (index)
    # end of array (index)
    # count: count containing number of smaller elements to the right of the number
    
    # Edge case
    if left >= right:
        return 
    
    # find mid and split the list to sort
    mid = (right + left) // 2
    print(mid)

    mergeSort(arr, left, mid, count, ind)
    mergeSort(arr, mid + 1, right, count, ind)

    l = left 
    l1 = mid+1
    cnt = 0 # number of elements in the right side smaller to the current index
    s = []

    while l <= mid and l1 <= right:
        if arr[ind[l]] <= arr[ind[l1]]:
             s.append(ind[l])
             count[ind[l]] += cnt
             l += 1
        else:
            s.append(ind[l1])
            cnt += 1
            l1 += 1

    # consider leftovers
    if l > mid:
        while l1 <= right:
            s.append(ind[l1])
            l1 += 1

    if l1 > right:
        while l <= mid:
            s.append(ind[l])
            count[ind[l]] += cnt
            l += 1

    # update the index array
    for i in range(left, right+1):
        ind[i] = s[i - left] 

    # print(s)
    # print("-----Count Array----{}".format(count))

s=Solution()
print(s.solve([5, 2, 3, 4, 1]))