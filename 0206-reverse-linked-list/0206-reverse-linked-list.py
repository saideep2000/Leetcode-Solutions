# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        curr = None
        new = None
        while head:
            new = ListNode()
            new.val = head.val
            new.next = curr
            curr = new
            head = head.next
        return new