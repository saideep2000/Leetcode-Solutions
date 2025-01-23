class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        f = 0
        l = 0
        fresh = 0

        qu = collections.deque()

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 2:
                    qu.append((i, j))
                elif grid[i][j] == 1:
                    fresh = fresh + 1

        while qu:
            curr = len(qu)
            for i in range(0,curr):
                x, y = qu.popleft()
                for dx, dy in moves:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] < grid[x][y] and grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        qu.append((x+dx, y+dy))
                        f = f + 1
            l = l + 1
        print(fresh, f)
        if fresh == 0:
            return 0
        elif fresh - f == 0:
            return l-1
        else:
            return -1
        