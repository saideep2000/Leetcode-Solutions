# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        rem = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(rem, (node.val, i, node))
        final_head = ListNode(0)
        current = final_head
        while rem:
            val, i, curr_node = heapq.heappop(rem)
            current.next = curr_node
            if curr_node.next != None:
                heapq.heappush(rem, (curr_node.next.val, i, curr_node.next))
            current = current.next
        return final_head.next