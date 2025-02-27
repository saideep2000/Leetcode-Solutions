# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return Solution.rec(self, root, root.val)
    def rec(self, root, maxi):
        if root:
            count = 0
            if root.val >= maxi:
                count = count + 1
            maxi = max(root.val, maxi)
            count = count + Solution.rec(self, root.left, maxi) + Solution.rec(self, root.right, maxi)
            return count
        else:
            return 0