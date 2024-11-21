class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # d = {}
        store = []
        heapq.heapify(store)
        for i in points:
            temp = ((i[0]*i[0]) + (i[1]*i[1]))
            heapq.heappush(store, (temp, i))
            # d[(temp, tuple(i))] = i
        f = []
        print(store)
        while k != 0:
            temp , point = heapq.heappop(store)
            f.append(point)
            k = k - 1
        return f