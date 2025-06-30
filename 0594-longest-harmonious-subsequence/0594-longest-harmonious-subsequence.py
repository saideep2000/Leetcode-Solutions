class Solution:
    def findLHS(self, nums: List[int]) -> int:
        store_counts = defaultdict(int)
        for i in range(0,len(nums)):
            store_counts[nums[i]] = store_counts[nums[i]] + 1
        sorted_store = dict(sorted(store_counts.items()))

        previous = None
        result = 0
        for key, value in sorted_store.items():
            if previous == None:
                previous = key
            else:
                if key - previous == 1:
                    result = max(result , sorted_store[previous] + value)
                previous = key
        return result