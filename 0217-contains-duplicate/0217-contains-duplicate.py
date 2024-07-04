import collections as cl
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=cl.Counter(nums)
        for k,v in c.items():
            if v>1:
                return True