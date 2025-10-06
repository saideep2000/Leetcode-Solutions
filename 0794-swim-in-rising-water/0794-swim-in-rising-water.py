class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        moves = [[0,1], [1,0], [-1,0], [0, -1]]
        visited = set()

        pQ = [(grid[0][0], 0 ,0)]
        heapq.heapify(pQ)

        while pQ:
            depth, i, j = heapq.heappop(pQ)

            result = max(result, depth)

            if i == n-1 and j == n-1:
                return result
            
            for mx, my in moves:
                if 0 <= i+mx < n and 0 <= j+my < n and (i+mx, j+my) not in visited:
                    visited.add((i+mx, j+my))
                    heapq.heappush(pQ, (grid[i+mx][j+my], i+mx, j+my))


