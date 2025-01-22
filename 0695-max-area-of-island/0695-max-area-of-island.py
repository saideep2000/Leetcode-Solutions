class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def backtrack(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            noofones = 1
            grid[i][j] = 0

            for dx, dy in moves:
                temp = backtrack(i + dx, j + dy)
                noofones = noofones + temp
            return noofones


        ma = 0
        for p in range(0,m):
            for q in range(0, n):
                if grid[p][q] == 1:
                    ma = max(ma,backtrack(p,q))
        return ma