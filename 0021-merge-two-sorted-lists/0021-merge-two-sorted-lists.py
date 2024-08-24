# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        new = ListNode()
        curr = None
        head = None
        while list1 and list2:
            new = ListNode()
            if list1.val > list2.val:
                new.val = list2.val
                list2 = list2.next
            else:
                new.val = list1.val
                list1 = list1.next

            if curr:
                curr.next = new
            else:
                head = new
            curr = new
        if list1:
            new.next = list1
        if list2:
            new.next = list2
        print(list1)
        print(list2)
        return head