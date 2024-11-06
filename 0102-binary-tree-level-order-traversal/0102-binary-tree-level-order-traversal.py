# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return Solution.rec(self, root)
    def rec(self, root):
        if root == None:
            return []
        temp = [root.val]
        merge = []
        merge.append(temp)
        temp1 = Solution.rec(self,root.left)
        temp2 = Solution.rec(self,root.right)
        if temp1 == []:
            if temp2 == []:
                return merge
            else:
                return merge + temp2
        else:
            if temp2 == []:
                return merge + temp1
            else:
                temp1 = Solution.combine_lists(self, temp1, temp2)
                return merge + temp1
    def combine_lists(self, list1, list2):
        combined = []
        max_len = max(len(list1), len(list2))
        
        for i in range(max_len):
            if i < len(list1) and i < len(list2):
                combined.append(list1[i] + list2[i])
            elif i < len(list1):
                combined.append(list1[i])
            else:
                combined.append(list2[i])
                
        return combined
        
        
