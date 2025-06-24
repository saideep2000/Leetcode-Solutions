# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def traverseTree(head):
            nonlocal count, result
            if result != None:
                return 
            if head == None:
                return 
            traverseTree(head.left)

            count = count + 1
            if count == k:
                result = head.val
                
            traverseTree(head.right)
            

        traverseTree(root)
        return result