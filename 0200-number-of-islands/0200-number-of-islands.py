class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def backtrack(p, q):
            if p < 0 or p >= m or q < 0 or q >= n or grid[p][q] == "0":
                return
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            grid[p][q] = "0"

            for dx, dy in moves:
                backtrack(p + dx, q + dy)
            return

        f = 0
        for i in range(0,m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    backtrack(i, j)
                    f = f + 1
        return f