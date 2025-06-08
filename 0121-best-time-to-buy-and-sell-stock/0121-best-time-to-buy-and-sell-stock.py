class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        final_profit = 0
        curr_max = prices[-1]

        for i in range(len(prices)-2,-1,-1):
            final_profit = max(final_profit, (curr_max - prices[i]))
            curr_max = max(curr_max, prices[i])
        return final_profit