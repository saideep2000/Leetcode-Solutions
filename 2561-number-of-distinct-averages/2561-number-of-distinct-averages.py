class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        nums = sorted(nums)
        i,j = 0,len(nums)-1
        while i<j:
            s.add(nums[i]+nums[j])
            i = i + 1
            j = j - 1
        return len(s)