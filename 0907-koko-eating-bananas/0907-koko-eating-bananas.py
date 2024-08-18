class Solution:
    def maths(k, piles):
        sum = 0
        for i in piles:
            sum = sum + math.ceil(i/k)
        return sum
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        rem = 0
        while lo <= hi:
            m = (lo+hi)//2
            if Solution.maths(m, piles) <= h:
                rem = m
                hi = m - 1
            elif Solution.maths(m, piles) > h:
                lo = m + 1
        return rem
            