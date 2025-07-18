"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# for every node i will create the new duplicate and keep it in the dict
# {old1: new1, old2: new2, ...}

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        # create the duplicates and store it the hashmap
        hm = defaultdict()

        temp = head

        while temp:
            hm[temp] = Node(temp.val)
            temp = temp.next
        

        # let's loop it out the linked list and attach the next and random for the new once
        temp = head

        while temp:
            if temp.next == None:
                hm[temp].next = None
            else:
                hm[temp].next = hm[temp.next]

            if temp.random == None:
                hm[temp].random = None
            else:
                hm[temp].random = hm[temp.random]

            temp = temp.next
        
        return hm[head]


