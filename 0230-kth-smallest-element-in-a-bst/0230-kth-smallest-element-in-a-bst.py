# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = []
        temp = Solution.rec(self, root, temp)
        # temp = sorted(temp)
        return temp[k-1]
    def rec(self, root, temp):
        if root == None:
            return temp
        temp = Solution.rec(self, root.left, temp)
        temp.append(root.val)
        temp = Solution.rec(self, root.right, temp)
        return temp