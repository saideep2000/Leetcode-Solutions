class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = []
        rem = 0
        for i in range(0,len(nums)):
            if len(store) == 0:
                if target - nums[i] in nums[i+1:]:
                        rem = target - nums[i]
                        store.append(i)
            else:
                if rem == nums[i]:
                    store.append(i)
        return store



        