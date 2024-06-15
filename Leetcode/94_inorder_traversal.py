# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderHelper(self, root: Optional[TreeNode], res: List[int]):
        if not root:
            return 
        self.inorderHelper(root.left, res)
        res.append(root.val)
        self.inorderHelper(root.right, res)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorderHelper(root, res)
        return res
        
        