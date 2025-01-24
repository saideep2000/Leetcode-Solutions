class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 or j == 0:
                    pacific.add((i,j))
                if i == m-1 or j == n-1:
                    atlantic.add((i,j))
        con_pacific = set()
        con_atlantic = set()
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        # this itreate through all possible elements it can reach and add it to the contribution set
        def dfs(x,y, con):
            con.add((x,y))
            for mx, my in moves:
                if 0 <= x+mx < m and 0 <= y+my < n and heights[x+mx][y+my] >= heights[x][y] and (x+mx,y+my) not in con:
                    dfs(x+mx, y+my, con)
                

        for px,py in pacific:
            dfs(px,py,con_pacific)

        for px,py in atlantic:
            dfs(px,py,con_atlantic)
            
        common = con_pacific.intersection(con_atlantic)

        return [i for i in common]