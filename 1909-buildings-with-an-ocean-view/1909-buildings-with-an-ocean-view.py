class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        rem = 0
        li = []
        for i in range(len(heights) -1 , -1, -1):
            if heights[i] > rem:
                li.append(i)
                rem = max(rem, heights[i])
            
        return li[::-1]