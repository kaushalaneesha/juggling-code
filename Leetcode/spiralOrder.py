class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers

    def spiralOrderOld(self, A):
        res = []
        round = 0
        M = len(A) # rows
        N  = len(A[0]) #columns
        count = M * N
        cc = 0 # current count

        def addElem(elem, cc): 
            if cc < count:
                res.append(elem)
                cc += 1
            return cc

        while cc < count:
            for j in range(round, N - round):
                cc = addElem(A[round][j], cc)
            for i in range(round + 1, M - round):
                cc = addElem(A[i][N-round-1], cc)
            for j in range(N-round-2, round-1, -1):
                cc = addElem(A[M-round-1][j], cc)
            for i in range(M-round-2, round, -1):
                cc = addElem(A[i][round], cc)
            round += 1
        return res
    
    def spiralOrder(self, matrix):
        res = []
        # There are 4 directions
        # lr 
        # ud
        # rl
        # du
        direction = "lr"
        m = len(matrix)
        n = len(matrix[0])
        count = m * n
        start_row = 0
        end_row = m - 1
        start_col = 0 
        end_col = n - 1

        print(count)
        print(end_row)
        print(end_col)

        while count > 0:
            print(res)
            if direction == "lr":
                # print("hii")
                for i in range(start_col, end_col+1):
                    res.append(matrix[start_row][i])
                    count -= 1
                start_row += 1
                direction = "ud"
                # print(direction)
            elif direction == "ud":
                for i in range(start_row, end_row+1):
                    res.append(matrix[i][end_col])
                    count -= 1
                end_col -= 1
                direction = "rl"
                # print(direction)
            elif direction == "rl":
                for i in range(end_col, start_col-1, -1):
                    res.append(matrix[end_row][i])
                    count -= 1
                direction = "du"
                end_row -= 1
            elif direction == "du":
                for i in range(end_row, start_row-1, -1):
                    res.append(matrix[i][start_col])
                    count -= 1
                direction = "lr"
                start_col += 1 
        return res
    
            
s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))