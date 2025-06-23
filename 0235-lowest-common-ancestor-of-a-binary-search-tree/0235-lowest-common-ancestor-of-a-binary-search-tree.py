# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # def traverseTree(head):
        #     if head == None:
        #         return (False, None)
            
        #     found_l, lca_l = traverseTree(head.left)
        #     found_r, lca_r = traverseTree(head.right)

        #     if lca_l or lca_r:
        #         if lca_l != None:
        #             return (True, lca_l)
        #         else:
        #             return (True, lca_r)
            
        #     if found_l and found_r:
        #         return (True, head)
            
        #     if found_l or found_r:
        #         if head == p or head == q:
        #             return (True, head)
        #         return (True, None)
            
        #     if head == p or head == q:
        #         return (True, None)
            
        #     return (False, None)

        
        # found, result = traverseTree(root)

        # return result

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root