class Solution:
    def maths(k, piles):
        sum = 0
        for i in piles:
            sum = sum + math.ceil(i/k)
        return sum
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 0
        hi = max(piles)
        rem = 0
        while lo <= hi:
            m = (lo+hi)//2
            if Solution.maths(m+1, piles) <= h:
                rem = m+1
                hi = m - 1
            elif Solution.maths(m+1, piles) > h:
                lo = m + 1
        return rem
            