import collections
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return a list of integers
    def answerQueries(self, A, B, C):
        paths = dict()
        # Create graph 
        graph = collections.defaultdict(set)
        for a, b in B:
            graph[a].add(b)
            graph[b].add(a)

        def get_path(start, end):
            print("get path")
            visited = set()
            q = [(start, [start])]
            while q:
                node, path = q.pop(0)
                if node == end:
                    return path
                if node not in visited: 
                    visited.add(node)
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            q.append((neighbour, path + [neighbour]))
        
        res = []
        for start, end, target in C:
            # Step 1: Find the path from start to end (using bfs)
            if (start, end) in paths:
                path = paths.get((start, end))
            else:
                path = set(get_path(start, end))
                paths[(start, end)] = path
                paths[(end, start)] = path

            # path = set(get_path(start, end))


            visited = set()
            q = [target]
            while q:
                node = q.pop(0)
                if node in path:
                    res.append(node)
                    break
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        q.append(neighbour)
        return res



        

s = Solution()
A = 6
B = [[1, 4], 
     [1, 2], 
     [1, 3],
     [3, 5],
     [3, 6]
     ]
C = [[2, 5, 6], [5, 2, 6], [5, 2, 1], [2, 5, 4]]
print(s.answerQueries(A, B, C))
