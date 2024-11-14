# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            last = q[-1]
            if last:
                res.append(last.val)
            for i in range(qlen):
                temp = q.popleft()
                if temp:
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
        return res