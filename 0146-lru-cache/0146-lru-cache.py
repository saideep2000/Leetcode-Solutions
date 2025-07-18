class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0, 0, None, None)
        self.tail = ListNode(0, 0, self.head, None)
        self.head.next = self.tail
        
        self.hm = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hm:
            # Make the node most recently used (move to front)
            temp = self.hm[key]
            self.delNode(temp)
            self.addToFront(temp)
            return temp.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            # Update existing key
            temp = self.hm[key]
            self.delNode(temp)
            temp.val = value
            self.addToFront(temp)
        else:
            # Add new key
            if len(self.hm) >= self.capacity:
                # Remove least recently used (node before tail)
                lru_node = self.tail.prev
                self.delNode(lru_node)
                del self.hm[lru_node.key]
            
            # Create new node and add to front
            new_node = ListNode(key, value)
            self.addToFront(new_node)
            self.hm[key] = new_node

    def delNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToFront(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node