class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bfs(li):
            l,r = 0, len(li)-1
            while l <= r:
                middle = l + ((r-l)//2)
                if li[middle] == target:
                    return True
                elif li[middle] > target:
                    r = middle - 1
                elif li[middle] < target:
                    l = middle + 1
            return False
        
        for each_list in matrix:
            if target >= each_list[0] and target <= each_list[-1]:
                return bfs(each_list)
        return False