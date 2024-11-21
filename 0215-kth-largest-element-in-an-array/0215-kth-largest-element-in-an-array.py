class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        store = [-i for i in nums]
        heapq.heapify(store)
        while k != 1:
            heapq.heappop(store)
            k = k - 1
        return -store[0]