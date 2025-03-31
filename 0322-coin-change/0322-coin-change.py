class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hm = {}
        def dfs(c, a):
            if a < 0:
                return -1
            if a == 0:
                return 0
            
            # use memoization
            if a in hm:
                return hm[a]
            steps = float('+inf')
            for coin in c:
                if a >= coin:
                    result = dfs(c, a - coin)
                    if result != -1:
                        steps = min(steps, result + 1)
            
            if steps == float(+inf):
                hm[a] = -1
                return -1
            else:
                hm[a] = steps
                return steps
        
        return dfs(sorted(coins), amount)