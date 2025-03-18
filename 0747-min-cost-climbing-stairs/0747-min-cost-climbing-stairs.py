class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_one, min_cost_two = 0, 0
        for i in range(2, len(cost)+1):
            min_cost = min(min_cost_one + cost[i-2], min_cost_two + cost[i-1])
            min_cost_one = min_cost_two
            min_cost_two = min_cost
        return min_cost_two