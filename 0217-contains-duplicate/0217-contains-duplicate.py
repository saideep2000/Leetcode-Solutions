class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rem = {}
        for i in nums:
            if i not in rem.keys():
                rem[i] = 1
            else:
                return True
        return False