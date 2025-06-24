class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Get all the indexes where the key match.
        # Values of j - these are indexes.
        # These are already sorted
        store = []
        for i in range(len(nums)):
            if nums[i] == key:
                store.append(i)
        
        # now make the result
        result = []
        current = 0
        i = 0
        while i < len(nums):
            if current >= len(store):
                break
            
            if abs(i - store[current]) > k:
                if i < store[current]:
                    i = i + 1
                else:
                    current = current + 1
            elif abs(i - store[current]) <= k:
                result.append(i)
                i = i + 1

        return result