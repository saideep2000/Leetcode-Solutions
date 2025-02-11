class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = collections.defaultdict()
        for i in range(0,len(nums)):
            h[nums[i]] = i
        print(h)
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in h and i != h[complement]:
                return [i, h[complement]]
