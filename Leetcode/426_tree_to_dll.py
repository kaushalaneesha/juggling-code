
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        """
        def helper(node: Node):
            nonlocal first, last

            if not node:
                return 
            
            if node:
                helper(node.left)

                # If last is present update this nodes
                # left to point to last
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node

                # update the last element for the next round. 
                last = node

                helper(node.right)

        if not root:
            return
        
        first, last = None, None
        helper(root)

        # Link the first(smallest) and last(largest) nodes at the end
        last.right = first
        first.left = last

        return first
        