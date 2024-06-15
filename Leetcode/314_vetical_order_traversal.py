# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            Intuition
            Traverse the map in order.
            Create a map of column number and nodes of that column.
            Column left will be column - 1 and right will be column + 1

            Inorder doesnt result in correct row order. Better to do a BFS so that we go row by row.

            Approach
            Do BFS and populate make containing column and its nodes.

            Complexity
            Time complexity:O(n)
            Space complexity: O(n)
        """
        column_map = collections.defaultdict(list)
        keys = set()
        queue = []
        queue.append((root, 0))
        while queue:
            node, col_num = queue.pop(0)
            if node:
                column_map[col_num].append(node.val)
                keys.add(col_num)
                if node.left:
                    queue.append((node.left, col_num - 1))
                if node.right:
                    queue.append((node.right, col_num + 1))

        k_lst = list(keys)
        k_lst.sort()
        res = []
        for i in k_lst:
            res.append(column_map[i]) 
        return res

        
        