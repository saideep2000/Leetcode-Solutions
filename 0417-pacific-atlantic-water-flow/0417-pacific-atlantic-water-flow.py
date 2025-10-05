class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        result = []

        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        storePacific = set()
        storeAtlantic = set()

        def dfsPacific(x, y):
            nonlocal storePacific

            storePacific.add((x,y))

            for mx, my in moves:
                nx, ny = x+mx, y+my
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in storePacific and heights[x][y] <= heights[nx][ny]:
                    dfsPacific(nx, ny)
        
        def dfsAtlantic(x, y):
            nonlocal storeAtlantic

            storeAtlantic.add((x,y))

            for mx, my in moves:
                nx, ny = x+mx, y+my
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in storeAtlantic and heights[x][y] <= heights[nx][ny]:
                    dfsAtlantic(nx, ny)
        
        # let's itreate through the pacific
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfsPacific(i, j)

        # let's itreate through the atlantic
        for i in range(m):
            for j in range(n):
                if i == m-1 or j == n-1:
                    dfsAtlantic(i, j)

        
        # itreate through 1 and see other 1
        for x,y in storePacific:
            if (x,y) in storeAtlantic:
                result.append([x,y])

        return result