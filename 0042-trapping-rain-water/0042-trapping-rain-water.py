class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)

        l,r = 0,len(height)-1
        running_max_left = 0
        running_max_right = 0
        while l<len(height):

            max_left[l] = running_max_left
            running_max_left = max(running_max_left, height[l])
            
            max_right[r] = running_max_right
            running_max_right = max(running_max_right, height[r])
            
            l = l + 1
            r = r - 1

        trapped = 0
        i = 0
        while i < len(height):
            temp = min(max_left[i], max_right[i])-height[i]
            if temp > 0:
                trapped = trapped + temp
            i = i + 1

        return trapped