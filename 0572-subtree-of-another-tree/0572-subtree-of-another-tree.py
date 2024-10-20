# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        temp = Solution.rec(self, root, subRoot)
        if temp == True:
            return True
        else:
            return False

    def rec(self, root, subRoot):
        if root == None:
            return None
        if root.val == subRoot.val:
            if Solution.sameTree(self, root, subRoot):
                return True
        curr = Solution.rec(self, root.left, subRoot)
        if curr:
            return True
        curr = Solution.rec(self, root.right, subRoot)
        return curr

    def sameTree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None:
            print(root1.val, root2.val)
            curr = False
            if root1.val == root2.val:
                curr = Solution.sameTree(self, root1.left, root2.left)
                if curr:
                    curr = Solution.sameTree(self, root1.right, root2.right)
                else:
                    return curr
            return curr
        else:
            return False