class Solution:
    def binarySearch(target, li):
        l = 0
        r = len(li)-1
        while l <= r :
            m = (l+r)//2
            if li[m] == target:
                return True
            elif li[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            if target <= matrix[i][len(matrix[i])-1]:
                return Solution.binarySearch(target, matrix[i])
        return False