class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        curr = 1
        while curr <= n:
            n = n - curr
            curr = curr + 1
        
        return curr-1
