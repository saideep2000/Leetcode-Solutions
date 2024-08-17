class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        h = len(nums)-1
        while l <= h:
            m = (h+l)//2
            # if nums[l] == target:
            #     return l
            # if nums[h] == target:
            #     return h
            if nums[m] == target:
                return m
            if nums[m] > target:
                h = m - 1
                # l = l + 1
            else:
                l = m + 1
                # h = h - 1

        return -1