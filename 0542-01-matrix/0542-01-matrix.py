class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        qu = collections.deque()
        m = len(mat)
        n = len(mat[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        rem = set()

        for p in range(0,m):
            for q in range(0,n):
                if mat[p][q] == 0:
                    qu.append((p,q))
                else:
                    mat[p][q] = float('inf')
        
        while qu:
            x, y = qu.popleft()
            for dx, dy in moves:
                if 0 <= x+dx < m and 0 <= y+dy < n and mat[x+dx][y+dy] > mat[x][y]+1:
                    mat[x+dx][y+dy] = mat[x][y]+1
                    qu.append((x+dx, y+dy))
        
        return mat