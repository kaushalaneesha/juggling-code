# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid_bst_helper(node: TreeNode, min_val: int, max_val: int):
            # check if the node's value is within the min and max range. 
            # keep updating the min and max as we traverse the tree
            if not node:
                return True
            if node.val < min_val or node.val > max_val:
                # fail fast when we see a node with invalid value
                return False
            return valid_bst_helper(node.left, min_val, node.val - 1) and valid_bst_helper(node.right, node.val + 1, max_val)
            
        
        return valid_bst_helper(root, -2 ** 31, 2 ** 31 + 1)
        
        