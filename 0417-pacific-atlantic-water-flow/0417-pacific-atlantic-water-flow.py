class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(heights), len(heights[0])
        result = []
        pac, atl = set(), set()

        def dfs(x, y, visited, prev_height):
            if x < 0 or x >= m or y < 0 or y >= n or (x,y) in visited or heights[x][y] < prev_height:
                return
            visited.add((x,y))
            for mx, my in moves:
                dfs(x+mx, y+my, visited, heights[x][y])
        
        # for the row = 0 & row = m-1
        for col in range(n):
            dfs(0, col, pac, 0)
            dfs(m-1, col, atl, 0)
        
        # for the col = 0 & col = n-1
        for row in range(m):
            dfs(row, 0, pac, 0)
            dfs(row, n-1, atl, 0)
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])
        return result