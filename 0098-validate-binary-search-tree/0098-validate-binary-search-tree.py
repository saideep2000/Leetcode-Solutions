# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minn = float('-inf')
        maxx = float('inf')
        return Solution.rec(self, root, minn, maxx)
    def rec(self, root, minn, maxx):
        if root == None:
            return True
        if root.val >= maxx or root.val <= minn:
            return False
        temp1 = Solution.rec(self, root.left, minn, min(maxx, root.val))
        if temp1 == False:
            return False
        temp2 = Solution.rec(self, root.right, max(minn, root.val), maxx)
        if temp2 == False:
            return False
        if temp1 and temp2:
            return True
        else:
            return False