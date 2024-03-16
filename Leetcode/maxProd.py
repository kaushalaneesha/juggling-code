# def maxProduct(arr, n):
#     # code here
#     # 	N = 5
#     # Arr[] = {6, -3, -10, 0, 2}
#     # 		index      currProd        maxProd        
#     #         0          6               6
#     #         1          -18             6 
#     #         2          180             180
#     #         3          0               180  
#     #         4          2               180            if currProd == 0: currProd = arr[i]
#     currProd = 0
#     maxProd = 0
#     for num in arr:
#         print("{} {}".format(currProd, maxProd))
#         if currProd == 0:
#             currProd = num     # As we can't multiply with zero
#         else:
#             currProd = currProd * num
#         if currProd > maxProd:
#             maxProd = currProd
#     return maxProd

def maxProduct(a, n):
    def helper(arr):
        print(arr)
        currProd = 0
        maxProd = max(arr)
        for num in arr:
            currProd = currProd * num
            if currProd > maxProd:
                maxProd = currProd
            if currProd == 0:
                currProd = 1  
        return maxProd   
    return max(helper(a), helper(a[::-1]))

print(maxProduct([6, -3, -10, 0, 2], 5))