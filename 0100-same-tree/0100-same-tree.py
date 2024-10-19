class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return Solution.rec(self, p,q)

    def rec(self, p, q):
        if p == None and q == None:
            return True
        elif p != None and q != None:
            curr = False
            if p.val == q.val:
                curr = Solution.rec(self, p.left, q.left)
                if curr:
                    curr = Solution.rec(self, p.right,q.right)
                else:
                    return curr
            return curr
        else:
            return False