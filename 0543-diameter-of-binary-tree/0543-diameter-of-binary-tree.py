# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h,m = Solution.rec(self,root)
        return m
    def rec(self, root):
        if root == None:
            return -1, 0
        h1, m1 = self.rec(root.left)
        h2, m2 = self.rec(root.right)
        h1 = h1 + 1
        h2 = h2 + 1
        h = max(h1,h2)
        m = h1 + h2
        m = max(m, m1, m2)
        return h,m
