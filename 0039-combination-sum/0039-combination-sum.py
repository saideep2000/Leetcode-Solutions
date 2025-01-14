class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        f = []
        def dfs(i,curr, subset):
            if i >= len(candidates) or sum(subset) > target:
                return
            elif sum(subset) == target:
                f.append(subset.copy())
                return
            subset.append(candidates[i])
            dfs(i,curr+candidates[i],subset)
            subset.pop()
            dfs(i+1, curr, subset)
        dfs(0,0,[])
        return f
        