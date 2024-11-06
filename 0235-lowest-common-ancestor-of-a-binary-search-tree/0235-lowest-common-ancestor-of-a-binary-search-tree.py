# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            temp = root.val
            if root.val > p.val:
                if root.val < q.val:
                    return root
                elif root.val > q.val:
                    root = root.left
                else:
                    return root
            elif root.val < p.val:
                if root.val > q.val:
                    return root
                elif root.val < q.val:
                    root = root.right
                else:
                    return root
            else:
                return root
