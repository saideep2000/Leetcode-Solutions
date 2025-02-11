class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = collections.defaultdict()
        for i in range(0,len(nums)):
            com = target - nums[i]
            if com in h:
                return [i,h[com]]
            h[nums[i]] = i