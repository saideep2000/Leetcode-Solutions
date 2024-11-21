class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        store = [-i for i in nums]
        heapq.heapify(store)
        while k != 1:
            heapq.heappop(store)
            k = k - 1
        if store[0] < 0:
            return abs(store[0])
        else:
            return -store[0]
        return abs(store[0])