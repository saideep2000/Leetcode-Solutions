class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        0 1 2 3 4 5 6 7 _8_ = 9 length
        target = 8
        
        """
        l,r = 0,len(nums)-1
        while l <= r:
            middle = l + ((r-l)//2) # (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        return -1
