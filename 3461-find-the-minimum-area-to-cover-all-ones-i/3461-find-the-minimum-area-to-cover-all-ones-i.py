class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        minI, maxI, minJ, maxJ = m-1, 0, n-1, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minI = min(minI, i)
                    minJ = min(minJ, j)
                    maxI = max(maxI, i)
                    maxJ = max(maxJ, j)

        

        area = (maxI - minI + 1) * (maxJ - minJ + 1)

        return area