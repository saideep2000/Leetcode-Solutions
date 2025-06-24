# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverseTree(head):
            if head == None:
                return (True, None, None)
            
            status_l, min_val_l, max_val_l = traverseTree(head.left)
            status_r, min_val_r, max_val_r = traverseTree(head.right)

            if not status_l or not status_r:
                return (False, min_val_l, max_val_r)
            
            if max_val_l != None:
                if head.val <= max_val_l:
                    return (False, min_val_l, max_val_r)
            if min_val_r != None:
                if head.val >= min_val_r:
                    return (False, min_val_l, max_val_r)
            

            return (True, min_val_l if min_val_l else head.val, max_val_r if max_val_r else head.val)
        status, min_val, max_val = traverseTree(root)
        return status