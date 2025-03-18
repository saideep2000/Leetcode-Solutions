# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_val = 0
        flag = 0
        while l1 or l2 or prev_val:
            if l1 != None and l2 != None:
                temp = l1.val + l2.val + prev_val
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                temp = l1.val + prev_val
                l1 = l1.next
            elif l1 == None and l2 != None:
                temp = l2.val + prev_val
                l2 = l2.next
            else:
                temp = prev_val
            
            prev_val = 0

            # validating the sum and carry forward and add to the linkedlist
            if temp >= 10:
                prev_val = temp//10
                now = temp%10
            else:
                now = temp
            node = ListNode(now)
            
            if flag == 0:
                head = node
                flag = flag + 1
                prev = node
            else:
                prev.next = node
                prev = prev.next
        

        return head