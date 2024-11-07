# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        temp = Solution.rec(self, root)
        print(temp)
        f = []
        for i in temp:
            f.append(i[0])
        return f
    def rec(self, root):
        if root == None:
            return []
        temp = [root.val]
        temp1 = Solution.rec(self, root.left)
        temp2 = Solution.rec(self, root.right)
        merge = []
        merge.append(temp)
        if temp2:
            if temp1:
                # only keep last when merged
                temp1 = Solution.combine(self, temp1, temp2)
                return merge + temp1
            else:
                return merge + temp2
        else:
            if temp1:
                return merge + temp1
            else:
                return merge
    def combine(self, list1, list2):
        combined = []
        max_len = max(len(list1), len(list2))

        for i in range(max_len):
            if i < len(list2):
                combined.append(list2[i])
            elif i < len(list1) and i < len(list2):
                combined.append(list1[i] + list2[i])
            else:
                combined.append(list1[i])
                
        return combined