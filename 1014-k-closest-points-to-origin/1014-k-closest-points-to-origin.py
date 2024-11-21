class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        heapq.heapify(store)
        for i in points:
            temp = (i[0] ** 2) + (i[1] ** 2)
            heapq.heappush(store, (temp, i))
        f = []
        while k != 0:
            temp , point = heapq.heappop(store)
            f.append(point)
            k = k - 1
        return f