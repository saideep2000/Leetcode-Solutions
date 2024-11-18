# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        curr = root
        count = 0
        
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            count += 1
            
            if count == k:
                return curr.val
            
            curr = curr.right
