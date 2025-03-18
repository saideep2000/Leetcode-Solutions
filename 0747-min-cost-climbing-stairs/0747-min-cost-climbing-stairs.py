class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20] n = 3
        n = len(cost)
        min_cost = [0]*(n+1)
        min_cost[0], min_cost[1] = 0, 0
        
        for i in range(2,n+1):
            min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
        return min_cost[n]
