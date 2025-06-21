# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        sec_half = slow.next
        slow.next = None

        right = None
        while sec_half:
            temp = sec_half.next
            sec_half.next = right
            right = sec_half
            sec_half = temp
        
        left = head

        # merge
        while right:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left = temp1
            right = temp2