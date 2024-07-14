class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        m = 0
        premax = 0
        for i in range(len(prices)-1, -1, -1):
            m = premax - prices[i]
            if pro < m:
                pro = m
            premax = max(premax, prices[i])
        return pro