# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        mer = head

        # start merging
        while list1 and list2:
            if list1.val <= list2.val:
                mer.next = list1
                list1 = list1.next
            else:
                mer.next = list2
                list2 = list2.next
            mer = mer.next
        
        if list1:
            mer.next = list1
            list1 = list1.next
        elif list2:
            mer.next = list2
            list2 = list2.next


        return head.next