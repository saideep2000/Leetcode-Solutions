class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i in range(0,len(nums)):
            if target-nums[i] in rem.keys():
                return [i, rem[target-nums[i]]]
            rem[nums[i]] = i
