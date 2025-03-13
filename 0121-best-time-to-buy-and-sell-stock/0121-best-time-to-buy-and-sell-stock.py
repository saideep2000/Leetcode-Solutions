class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        pro = 0
        while i < len(prices) and j < len(prices):
            if prices[i] < prices[j]:
                pro = max(pro, (prices[j]-prices[i]))
                j = j + 1
            else:
                i = j
                j = j + 1
        return pro

