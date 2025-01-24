class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    row[i] = row[i] + 1
                    col[j] = col[j] + 1

        f = 0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        f = f + 1


        return f