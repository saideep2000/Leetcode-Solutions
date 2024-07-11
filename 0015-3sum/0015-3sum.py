class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        store = set()
        for i in range(0,len(nums)):
            j,k = i+1 ,len(nums)-1
            while j < k:
                if i == j or nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                elif i == k or nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                else:
                    trip = sorted([nums[i],nums[j], nums[k]])
                    store.add(tuple(trip))
                    j,k = j+1,k-1
        return store