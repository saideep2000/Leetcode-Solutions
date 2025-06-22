# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        store = deque([root])
        while store:
            current = store.popleft()
            if current != None:
                current.left, current.right = current.right, current.left
                if current.left:
                    store.append(current.left)
                if current.right:
                    store.append(current.right)

        return root