class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # [-4, -1, -1, 0, 1, 2]
        final = set()
        for initial in range(0,len(nums)-2):
            i, j = initial + 1, len(nums)-1
            while i < j:
                if nums[initial] + nums[i] + nums[j] > 0:
                    j = j - 1
                elif nums[initial] + nums[i] + nums[j] < 0:
                    i = i + 1
                else:
                    final.add((nums[initial], nums[i], nums[j]))
                    if nums[i] == nums[i+1]:
                        while i < j and nums[i] == nums[i+1]:
                                i = i + 1
                    else:
                        i = i + 1
        return list(final)