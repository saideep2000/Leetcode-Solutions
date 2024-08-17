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
        top = 0
        bottom = len(matrix)-1
        while top <= bottom:
            row = (top+bottom)//2
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                return Solution.binarySearch(target, matrix[row])
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                top = row + 1
        return False 