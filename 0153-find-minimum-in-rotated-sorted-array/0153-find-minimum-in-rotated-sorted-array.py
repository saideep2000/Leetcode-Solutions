class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        low_value = nums[0]

        while l < r:
            m = (l+r)//2

            low_value = min(low_value, nums[m])

            if nums[l] < nums[m]:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        if l == r:
            low_value = min(low_value, nums[l])
        return low_value