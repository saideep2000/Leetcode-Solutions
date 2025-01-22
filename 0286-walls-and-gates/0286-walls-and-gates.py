class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        qu = collections.deque()

        for p in range(0,m):
            for q in range(0,n):
                if rooms[p][q] == 0:
                    qu.append((p,q))
        while qu:
            dx, dy = qu.popleft()
            for modx, mody in moves:
                if 0 <= dx+modx < m and 0 <= dy+mody < n and rooms[dx+modx][dy+mody] != -1 and rooms[dx+modx][dy+mody] > rooms[dx][dy] + 1:
                    rooms[dx+modx][dy+mody] = rooms[dx][dy] + 1
                    qu.append((dx+modx, dy+mody))