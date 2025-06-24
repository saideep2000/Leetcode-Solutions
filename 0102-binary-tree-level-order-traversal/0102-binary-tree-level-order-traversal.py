# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # Handle edge case
            return []
            
        result = []
        store = deque([root])

        while store:
            initial = []
            temp = []
            for i in range(len(store)):
                initial.append(store[i].val)
                if store[i].left != None:
                    temp.append(store[i].left)
                if store[i].right != None:
                    temp.append(store[i].right)
            store = temp
            result.append(initial)
        return result

        # [[2,3], [4,5]] and [[1,0], [7,8]]
        # def merge2lists(l1, l2):
        #     reverse = False
        #     if len(l1) < len(l2):
        #         l1, l2 = l2, l1
        #         reverse = True
        #     for i in range(len(l2)):
        #         if l2[i] != []:
        #             if reverse:
        #                 l1[i] = l2[i] + l1[i]
        #             else:
        #                 l1[i].extend(l2[i])
            
        #     return l1

        # def traverseTree(head):
        #     if head == None:
        #         return []
        #     l_left = traverseTree(head.left)
        #     l_right = traverseTree(head.right)
        #     temp = []
        #     temp.append([head.val])
        #     if l_left != [] or l_right != []:
        #         temp.extend(merge2lists(l_left, l_right))
            
        #     return temp

        # return traverseTree(root)