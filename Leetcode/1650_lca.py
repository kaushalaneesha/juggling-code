"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor1(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Approach 1: 
        Save parents of both the nodes in seperate lists
        Iterate both the lists in reverse. Return the farthest common element found

        """
        def get_parents(node: Node) -> List[int]:
            parents = []
            while node:
                parents.append(node)
                node = node.parent
            return parents
        
        p_parents = get_parents(p)
        q_parents = get_parents(q)

        i = len(p_parents) - 1
        j = len(q_parents) - 1
        while i >= 0 and j >= 0 and p_parents[i].val == q_parents[j].val:
            i -= 1
            j -= 1
        
        return p_parents[i+1]
        
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Approach 2:
        Find difference of height
        """
        def find_depth(node: Node) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth
    
        p_depth = find_depth(p)
        q_depth = find_depth(q)

        if p_depth > q_depth:
            for _ in range(p_depth - q_depth):
                p = p.parent
        else:
            for _ in range(q_depth - p_depth):
                q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        
        return p
