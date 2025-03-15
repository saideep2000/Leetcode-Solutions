class DoubleLinkedList:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}  # Dictionary: key -> (value, node)
        
        # Dummy head & tail for easier operations
        self.head = DoubleLinkedList(0)  
        self.tail = DoubleLinkedList(0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Removes a node from the doubly linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        """Moves the node to the front (MRU position)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.hm:
            value, node = self.hm[key]
            
            # Move to the front only if it's not already there
            if self.head.next != node:  
                self._remove(node)
                self._add_to_front(node)
            
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            # If key exists, remove the old node
            _, node = self.hm[key]
            self._remove(node)

        # Add a new node to the front
        new_node = DoubleLinkedList(key, value)
        self._add_to_front(new_node)
        self.hm[key] = (value, new_node)  # Store in hashmap

        if len(self.hm) > self.cap:
            # Remove the LRU node (just before tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.hm[lru_node.key]  # Delete from hashmap
