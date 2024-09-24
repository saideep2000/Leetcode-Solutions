"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map original nodes to their corresponding copied nodes
        h = {}

        # Start the recursion
        temp, _ = self.rec(head, h)
        
        # After recursion completes, h contains all the node mappings
        
        # Assign the random pointers using the dictionary mapping
        current = head
        while current:
            if current in h and current.random:
                h[current].random = h[current.random]
            current = current.next

        return temp

    def rec(self, head, h):
        # Base case: if head is None, return None
        if not head:
            return None, h
        
        # If the node has already been copied, return the copy from the dictionary
        if head in h:
            return h[head], h
        
        # Create a new copy of the current node
        copy_node = Node(head.val)
        
        # Add the new node to the dictionary
        h[head] = copy_node

        # Recursively copy the next node
        copy_node.next, h = self.rec(head.next, h)
        
        # Return the copy of the node and the updated dictionary
        return copy_node, h

