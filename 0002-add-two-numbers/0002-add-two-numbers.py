# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.rec(l1,l2,0)

    def rec(l1,l2,carry):
        if l1 == None and l2 == None:
            if carry == 0:
                return None
            else:
                return ListNode(carry,None)

        temp = None
        if l1:
            l1_val = l1.val
            l1_next = l1.next
        else:
            l1_val = 0
            l1_next = None
        if l2:
            l2_val = l2.val
            l2_next = l2.next
        else:
            l2_val = 0
            l2_next = None

        add = l1_val + l2_val + carry
        if add/10 >= 1:
            carry = 1
            temp = ListNode(add % 10, Solution.rec(l1_next,l2_next,carry))
        else:
            temp = ListNode(add, Solution.rec(l1_next,l2_next,0))
        return temp