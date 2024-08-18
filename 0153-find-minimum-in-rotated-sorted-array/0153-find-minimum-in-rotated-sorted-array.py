class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if l == r:
            return nums[0]
        while l <= r:
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[m] < nums[-1]:
                r = m - 1
            if nums[m] > nums[-1]:
                l = m + 1
        return 0