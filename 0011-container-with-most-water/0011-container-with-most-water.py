class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l,r = 0, len(height)-1
        while l<r:
            compute = (min(height[l], height[r]) * (r-l))
            if compute > m:
                m = compute
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return m