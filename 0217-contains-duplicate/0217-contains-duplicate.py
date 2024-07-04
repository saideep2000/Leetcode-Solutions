class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rem = set()
        for i in nums:
            if i in rem:
                return True
            rem.add(i)
        return False