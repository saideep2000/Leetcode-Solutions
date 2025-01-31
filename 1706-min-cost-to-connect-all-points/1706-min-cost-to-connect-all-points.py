class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # let's try with min-heap and set
        visited = set()
        minHeap = [[0, points[0]]]
        m = 0 

        while len(visited) < len(points):
            dist, n = heapq.heappop(minHeap)
            if tuple(n) in visited:
                continue
            visited.add(tuple(n))
            m = m + dist
            for i in points:
                if i != n:
                    x1 = n[0]
                    y1 = n[1]
                    x2 = i[0]
                    y2 = i[1]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, i))
                    
        return m
