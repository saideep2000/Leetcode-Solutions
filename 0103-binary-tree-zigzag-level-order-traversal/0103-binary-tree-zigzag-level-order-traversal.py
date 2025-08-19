# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = deque([root])

        rev = -1

        while q:
            currLevelSize = len(q)
            temp = []
            for i in range(currLevelSize):
                curr = q.popleft()

                if not curr:
                    continue

                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

                temp.append(curr.val)
            
            if rev == 1:
                temp = temp[::-1]
            
            rev = rev * -1

            if temp != []:
                result.append(temp)
        
        return result
