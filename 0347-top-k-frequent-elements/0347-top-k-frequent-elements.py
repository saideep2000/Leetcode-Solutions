class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = defaultdict(int)

        for i in range(len(nums)):
            hm[nums[i]] = hm[nums[i]] + 1
        
        pq = []
        
        for num, times in hm.items():
            heapq.heappush(pq, (-times, num))
        
        result = []
        while len(result) != k :
            times, num = heapq.heappop(pq)
            result.append(num)
        
        return result

