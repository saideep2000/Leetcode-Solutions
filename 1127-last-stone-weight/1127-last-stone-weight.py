class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            temp1 = heapq.heappop(stones)
            temp2 = heapq.heappop(stones)
            val = temp1-temp2
            heapq.heappush(stones, val)
        return abs(stones[0])