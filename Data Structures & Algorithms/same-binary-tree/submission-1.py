# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both positions are empty
        if p is None and q is None:
            return True

        # One node exists while the other does not
        if p is None or q is None:
            return False

        # Values differ
        if p.val != q.val:
            return False

        # Both left subtrees and right subtrees must match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        