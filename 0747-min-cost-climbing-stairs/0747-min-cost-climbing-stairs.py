class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hm = defaultdict(int)
        def dp(n):
            if n <= 1:
                return 0
            if n not in hm:
                hm[n] = min(dp(n-1) + cost[n-1] , dp(n-2) + cost[n-2])
            return hm[n]

        return dp(len(cost))