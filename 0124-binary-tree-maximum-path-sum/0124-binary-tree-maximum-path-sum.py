# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.node_sum = float("-inf")
        
        
        def rec(node):
            if node == None:
                return 0
            left = max(rec(node.left), 0)
            right = max(rec(node.right), 0)
            path_to_pick = max(left, right)
            s = node.val + path_to_pick
            
            self.node_sum = max(self.node_sum, node.val, (node.val+ right + left))

            return s


        return max(rec(root), self.node_sum)