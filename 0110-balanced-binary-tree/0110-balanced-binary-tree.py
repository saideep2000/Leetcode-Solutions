# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            a = Solution.rec(self, root)
            if a == -1:
                return False
            else:
                return True
    def rec(self, root):
        if root == None:
            return 0
        h1 = self.rec(root.left)
        h2 = self.rec(root.right)
        if h1 == -1 or h2 == -1:
            return -1
        if abs(h1-h2) > 1:
            return -1
        return max(h1,h2) + 1
        