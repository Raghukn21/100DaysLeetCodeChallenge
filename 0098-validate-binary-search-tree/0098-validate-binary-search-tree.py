# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            # An empty tree/node is technically a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly within (low, high)
            if not (low < node.val < high):
                return False
            
            # Left child: must be less than current node.val (new high)
            # Right child: must be greater than current node.val (new low)
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Start with the full range of possible integer values
        return validate(root, float('-inf'), float('inf'))