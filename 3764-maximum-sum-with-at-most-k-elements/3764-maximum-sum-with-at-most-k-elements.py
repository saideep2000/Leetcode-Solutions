class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # let's first sort to get the highest elements
        for i in range(len(grid)):
            grid[i] = sorted(grid[i])

        # let's build the list by seeing the limit of each row
        store = []
        for i in range(len(grid)):
            grid_limit = len(grid[i]) - limits[i]
            store = store + grid[i][grid_limit:]
        store_length = len(store)

        # let's build the heap with the store
        heapq.heapify(store)

        # flush out the elements we don't need
        while store_length != k and store:
            heapq.heappop(store)
            store_length -= 1
        
        
        # Let's now capture the elements we need
        final_sum = 0
        while store:
            final_sum = final_sum + heapq.heappop(store)
        return final_sum