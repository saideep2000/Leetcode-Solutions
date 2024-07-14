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
                print(s)
            if maxLeft < height[i]:
                maxLeft = height[i]
            if maxRight < height[j]:
                maxRight = height[j]
            if maxLeft <= maxRight:
                i = i + 1
            else:
                j = j - 1
        return s


        # minleftright = [float('inf')] * len(height)
        # n = len(height)
        # maxLeft = 0
        # maxRight = 0
        # minleftright[0] = 0
        # minleftright[len(height)-1] = 0
        # s = 0
        # for i in range(n):
        #     minleftright[i] = maxLeft
        #     maxLeft = max(minleftright[i], height[i])
        # for i in range(n):
        #     minleftright[n-1-i] = min(maxRight, minleftright[n-1-i])
        #     maxRight = max(minleftright[n-1-i], height[n-1-i])
        # for i in range(len(minleftright)):
        #     v = minleftright[i] - height[i]
        #     if v > 0:
        #         s = s + v
        # return s