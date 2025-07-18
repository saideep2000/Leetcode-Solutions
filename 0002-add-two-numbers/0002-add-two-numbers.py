# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # [9,9,9,9,9,9,9]
        # [9,9,9,9]
        # [8,9,9,9,0,0,0,1] 

        head = ListNode()

        temp = head
        carry = 0

        # add till the smaller is exhausted
        while l1 and l2:
            value = l1.val + l2.val + carry

            if value >= 10:
                value = value - 10
                carry = 1
            else:
                carry = 0
            
            temp.next = ListNode(value)

            temp = temp.next
            l1 = l1.next 
            l2 = l2.next
        
        if l2 != None:
            l1 = l2
        
        while l1:
            value = l1.val + carry

            if value >= 10:
                value = value - 10
                carry = 1
            else:
                carry = 0
            
            temp.next = ListNode(value)

            temp = temp.next
            l1 = l1.next
        
        if carry == 1:
            temp.next = ListNode(1)
            temp = temp.next


        return head.next