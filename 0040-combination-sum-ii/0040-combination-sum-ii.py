class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        f = []
        subset = []
        candidates.sort()
        def dfs(i, total):
            if total > target:
                return
            if total == target:
                f.append(tuple(subset.copy()))
                return
            if i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            dfs(i+1, total)
        dfs(0,0)
        return f