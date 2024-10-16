# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        tmp1 = self.maxDepth(root.left)
        tmp2 = self.maxDepth(root.right)
        h = 1 + max(tmp1,tmp2)
        return h