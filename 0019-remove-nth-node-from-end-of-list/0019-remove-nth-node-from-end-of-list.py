# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        temp = ListNode()
        gap = 0
        while slow and fast and fast.next:
            if gap == 0:
                for i in range(0,n):
                    fast = fast.next
                gap = 1
            else:
                slow = slow.next
                fast = fast.next
        if slow == fast:
            return None
        if fast == None:
            return slow.next
        if slow.next:
            temp = (slow.next).next
            slow.next = temp
        return head