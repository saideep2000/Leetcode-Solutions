class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        def rec(n):
            if n == 0 or n == 1:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = min(rec(n-1)+cost[n-1], rec(n-2)+cost[n-2])
            return memo[n]
        return rec(len(cost))