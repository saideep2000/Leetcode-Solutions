class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[0,1], [1,0], [-1,0], [0,-1]]
        islands = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(self, row, col):
            # make the cell visited with -1
            grid[row][col] = -1

            # we will search for all 4 possible directions
            for mi, mj in moves:
                if row+mi >= 0 and col+mj >= 0 and row+mi < n and col+mj < m:
                    if grid[row+mi][col+mj] == "1":
                        dfs(self, row+mi, col+mj)
        
        # we'll itreate through all the islands i.e; 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(self, i, j)
                    islands = islands + 1
        return islands