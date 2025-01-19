from collections import defaultdict
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        m, n = len(board), len(board[0])
        
        # Find all starting points
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i, j))
        
        # Helper function for backtracking
        def backtrack(x, y, present, visited):
            # Base case: all characters matched
            if present == len(word):
                return True
            
            # Out of bounds or already visited or mismatch
            if x < 0 or x >= m or y < 0 or y >= n or visited[(x, y)] or board[x][y] != word[present]:
                return False
            
            # Mark current cell as visited
            visited[(x, y)] = True
            
            # Explore all possible moves
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in moves:
                if backtrack(x + dx, y + dy, present + 1, visited):
                    return True
            
            # Backtrack: unmark the current cell
            visited[(x, y)] = False
            return False
        
        # Iterate over all possible start points
        for sx, sy in start:
            visited = defaultdict(bool)
            if backtrack(sx, sy, 0, visited):
                return True
        
        return False