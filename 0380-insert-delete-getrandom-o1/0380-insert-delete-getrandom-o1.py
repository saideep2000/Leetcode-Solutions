

class RandomizedSet:

    def __init__(self):
        self.store = []
        self.track_store = {}
        self.total = 0

    def insert(self, val: int) -> bool:
        if val in self.track_store:
            return False
        self.store.append(val)
        self.track_store[val] = self.total
        self.total += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.track_store:
            return False
        # Get the index of the element to remove
        index_to_remove = self.track_store[val]
        # Get the last element in the list
        last_element = self.store[-1]
        # Move the last element to the position of the element to remove,
        # unless it's the same element
        if index_to_remove != self.total - 1:
            self.store[index_to_remove] = last_element
            self.track_store[last_element] = index_to_remove
        # Remove the last element from the list
        self.store.pop()
        # Remove the element from the dictionary
        del self.track_store[val]
        self.total -= 1
        return True

    def getRandom(self) -> int:
        # It's guaranteed that there is at least one element when this is called
        random_index = random.randint(0, self.total - 1)
        return self.store[random_index]
