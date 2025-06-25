# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val
        def traverseTree(head):
            nonlocal result
            if head == None:
                return 0
            left_val = traverseTree(head.left)
            right_val = traverseTree(head.right)

            result = max(result, left_val + head.val + right_val, head.val, left_val + head.val, head.val + right_val)
            
            return max(left_val + head.val, right_val + head.val, head.val)

        val = traverseTree(root)


        return max(result, val)