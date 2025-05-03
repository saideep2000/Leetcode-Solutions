class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = defaultdict()

        for i in range(0,len(nums)):
            rem = nums[i]
            if rem in store:
                return [store[rem], i]
            rem = target-nums[i]
            store[rem] = i

