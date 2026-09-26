# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, lower, upper):
            if node is None:
                return True

            # Current value must be strictly inside its valid range.
            if not (lower < node.val < upper):
                return False

            # Left subtree: values must be smaller than node.val
            # Right subtree: values must be greater than node.val
            return (
                validate(node.left, lower, node.val) and
                validate(node.right, node.val, upper)
            )

        return validate(root, float("-inf"), float("inf"))
        