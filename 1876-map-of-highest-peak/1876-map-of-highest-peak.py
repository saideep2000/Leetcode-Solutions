class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        qu = collections.deque()
        m = len(isWater)
        n = len(isWater[0])
        f = [[float('+inf') for _ in range(n)] for _ in range(m)]

        moves = [(0,1), (1,0), (0, -1), (-1, 0)]

        for p in range(0,m):
            for q in range(0, n):
                if isWater[p][q] == 1:
                    f[p][q] = 0
                    qu.append((p,q))
        while qu:
            x, y = qu.popleft()
            for dx, dy in moves:
                if 0 <= x+dx < m and 0 <= y+dy < n and f[x+dx][y+dy] > f[x][y] + 1:
                    f[x+dx][y+dy] = f[x][y] + 1
                    qu.append((x+dx, y+dy))
        return f