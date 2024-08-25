# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next

        # put the pointers to reverse 2nd half of list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        # reversing the 2nd half
        s_head = slow.next
        slow.next = None
        curr = None
        while s_head:
            temp = s_head.next
            s_head.next = curr
            curr = s_head
            s_head = temp
        
        # let's merge
        while head and curr:
            temp = head.next
            temp2 = curr.next
            head.next = curr
            curr.next = temp
            curr = temp2
            head = temp
        return head