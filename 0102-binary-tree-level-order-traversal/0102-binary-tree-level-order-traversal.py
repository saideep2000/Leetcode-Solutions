# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                temp = q.popleft()
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level:
                res.append(level)
        return res