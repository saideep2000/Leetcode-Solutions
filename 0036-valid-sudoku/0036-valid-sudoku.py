class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        s = collections.defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in s[str(i//3) + " "+str(j//3)]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    s[str(i//3) + " "+str(j//3)].add(board[i][j])
        return True