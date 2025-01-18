class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final = []
        def dfs(i,subset):
            if i >= len(nums):
                final.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            curr = i
            while i == curr:
                i = i + 1
            dfs(i, subset)
        dfs(0,[])
        rem = []
        for i in final:
            if i not in rem:
                rem.append(i)
        return rem
        # return final