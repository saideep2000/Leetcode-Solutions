# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = None

        def dfs(node):
            nonlocal answer
            if node.left == None and node.right == None:
                if node == p and node == q:
                    answer = node
                    return True, True
                elif node == p:
                    return True, False
                elif node == q:
                    return False, True
                else:
                    return False, False
            x, y = node == p, node == q
            if node.left:
                a, b = dfs(node.left)
                x = x or a
                y = y or b
            if node.right:
                a, b = dfs(node.right)
                x = x or a
                y = y or b
            
            if x and y and answer is None:
                answer = node
            print(node.val, x, y)
            return x,y


        dfs(root)
        
        return answer
        