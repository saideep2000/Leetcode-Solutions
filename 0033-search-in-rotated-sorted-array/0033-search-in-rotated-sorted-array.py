class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rem = -1
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            if target < nums[m]:
                if nums[m] > nums[l]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
            else:
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    if target < nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return rem
