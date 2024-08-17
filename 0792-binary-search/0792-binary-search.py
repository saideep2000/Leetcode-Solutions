class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0
        h = len(nums)-1
        m = math.floor((h+l)/2)
        i=1
        while l <= h:
            print(i)
            if nums[l] == target:
                return l
            if nums[h] == target:
                return h
            if nums[m] == target:
                return m
                
            if nums[m] > target:
                h = m - 1
                l = l + 1
            else:
                l = m + 1
                h = h - 1
            m = math.floor((h+l)/2)

            i=+1

        # if nums[l] == target:
        #     return l
        return -1