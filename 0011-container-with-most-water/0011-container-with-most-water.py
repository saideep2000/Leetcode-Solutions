class Solution:
    def maxArea(self, height: List[int]) -> int:
        final_max = 0
        i, j = 0, len(height)-1

        while i < j:
            temp = min(height[i], height[j]) * (j-i)
            
            final_max = max(final_max, temp)

            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return final_max