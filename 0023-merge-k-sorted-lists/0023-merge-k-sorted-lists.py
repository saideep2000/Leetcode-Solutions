# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoSortedLists(a, b) -> ListNode:
            dummy = ListNode(0)
            start = dummy
            while a and b:
                if a.val <= b.val:
                    dummy.next = a
                    a = a.next
                else:
                    dummy.next = b
                    b = b.next
                dummy = dummy.next

            dummy.next = a or b
            return start.next
        

        result = lists[0]
        for i in range(1, len(lists)):
            result = mergeTwoSortedLists(result,lists[i])
        
        return result