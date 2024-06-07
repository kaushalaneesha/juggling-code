import collections
import sys
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        def bfs(u, v):
            visited = set()
            q = [(u, 0)]
            while q:
                node, cost = q.pop(0)
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        if cc[u][neighbour] == -1:
                            cc[u][neighbour] = cost + 1
                        if neighbour == v:
                            return
                        else:
                            q.append((neighbour, cost + 1))
        
        n = len(A) + 1 + 1 # Since nodes are 1 indexed
        cc = [[-1 for i in range(n)] for j in range(n)]

        # make set of B
        bs = set(B)

        # Create a graph (adjacency list)
        graph = collections.defaultdict(set)
        for u, v in A:
            graph[u].add(v)
            graph[v].add(u)
            cc[u][v] = 1
            cc[v][u] = 1
        
        # Fill cc: cost of visiting (u,v)
        for i in range(1, n):
            for j in range(1, n):
                if i == j: # No cost of visting itself
                    cc[i][j] = 0
                elif cc[i][j] == -1:
                    bfs(i, j)
        

        min_cost = sys.maxsize
        for i in range(1, n):
            curr_cost = 0
            for j in range(1, n):
                if j in B:
                    curr_cost += cc[i][j]
            if curr_cost < min_cost:
                min_cost = curr_cost

        return min_cost
                

        
            
                    
s = Solution()
# A = [[2, 3], [1, 3]]
# B = [2]

A = [[1, 2], [3, 1], [6, 3], [5, 1], [4, 5], [7, 6]]
B = [5, 2, 3, 7, 1, 4]
print(s.solve(A, B))