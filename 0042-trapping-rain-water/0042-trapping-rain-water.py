class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        s = 0
        i,j = 0, len(height) -1
        while i<=j:
            if maxLeft <= maxRight:
                temp = maxLeft - height[i]
            else:
                temp = maxRight - height[j]
            if temp > 0:
                s = s + temp
            if maxLeft < height[i]:
                maxLeft = height[i]
            if maxRight < height[j]:
                maxRight = height[j]
            if maxLeft <= maxRight:
                i = i + 1
            else:
                j = j - 1
        return s