class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        
        for i in points:
            temp = (i[0] ** 2) + (i[1] ** 2)
            store.append([temp, i])
        heapq.heapify(store)
        f = []
        while k != 0:
            temp , point = heapq.heappop(store)
            f.append(point)
            k = k - 1
        return f