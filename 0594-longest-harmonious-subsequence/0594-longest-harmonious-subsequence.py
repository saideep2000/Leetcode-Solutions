class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        store_counts = defaultdict(int)
        for i in range(0,len(nums)):
            store_counts[nums[i]] = store_counts[nums[i]] + 1
            if nums[i] + 1 in store_counts:
                temp = store_counts[nums[i]] + store_counts[nums[i] + 1]
                result = max(result, temp)
            if nums[i] - 1 in store_counts:
                temp = store_counts[nums[i]] + store_counts[nums[i] - 1]
                result = max(result, temp)
        
        return result