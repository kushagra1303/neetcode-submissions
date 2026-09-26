# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Inorder(self,root,arr):
        if not root:
            return 
        
        self.Inorder(root.left,arr)
        arr.append(root.val)
        self.Inorder(root.right,arr)

        return 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.Inorder(root,arr)
        kSmallest = arr[k-1]
        return kSmallest
        