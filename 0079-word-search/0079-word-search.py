class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        s = word
        m = len(board)
        n = len(board[0])
        visited = [[0]*n for _ in range(0,m)]
        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        print(visited)

        def dfs(s : str, x : int, y : int) -> bool:
            if visited[x][y] == 1 or board[x][y] != s[0]:
                return False
            visited[x][y] = 1
            if len(s) == 1:
                return True
            for mx, my in moves:
                if x+mx >= 0 and y+my >=0 and x+mx < m and y+my < n:
                    if dfs(s[1:], x+mx, y+my):
                        return True
            visited[x][y] = 0
            return False

        for i in range(0,m):
            for j in range(0,n):
                if board[i][j] == word[0]:
                    if dfs(s,i,j):
                        return True

        return False