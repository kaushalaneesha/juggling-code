import collections
import sys
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        def bfs(key):
            visited = set()
            bs = set(B)
            total_cost = 0
            q = [(key, 0)] # Just an example (start_point, cost)
            while q:
                node, cost = q.pop(0)
                visited.add(node)
                for neighbour in graph[node]:
                    if not bs:
                        return total_cost
                    curr_cost = cost
                    if neighbour not in visited:
                        curr_cost += 1
                        if neighbour in bs:
                            total_cost += curr_cost
                            bs.remove(neighbour)
                        q.append((neighbour, curr_cost))
            return total_cost
        
        n = len(A) + 1 + 1 # Since nodes are 1 indexed
        cc = [[0 for i in range(n)] for j in range(n)]

        # make set of B
        
        # Create a graph (adjacency list)
        graph = collections.defaultdict(set)
        for u, v in A:
            graph[u].add(v)
            graph[v].add(u)
        
        # # Find min cost per node
        min_cost = sys.maxsize
        for key in graph: 
            cost = bfs(key)
            if cost < min_cost:
                min_cost = cost
        return min_cost
    

        
            
                    
s = Solution()
# A = [[2, 3], [1, 3]]
# B = [2]

A = [[1, 2], [3, 1], [6, 3], [5, 1], [4, 5], [7, 6]]
B = [5, 2, 3, 7, 1, 4]
print(s.solve(A, B))