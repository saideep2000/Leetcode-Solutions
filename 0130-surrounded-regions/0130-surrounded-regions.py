class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        rem = set()

        def dfs(x,y):
            board[x][y] = "T"
            for mx, my in moves:
                if 0 <= x+mx < m and 0 <= y+my < n and board[x+mx][y+my] == "O":
                    dfs(x+mx, y+my)
            return False
        
        for i in range(0,m):
            for j in [0,n-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for i in [0,m-1]:
            for j in range(0,n):
                if board[i][j] == "O":
                    dfs(i,j)

        for i in range(0,m):
            for j in range(0,n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
