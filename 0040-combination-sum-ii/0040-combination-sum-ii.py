class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        f = []
        candidates.sort()
        def dfs(i, curr, total):
            if total > target:
                return
            if total == target:
                f.append(tuple(curr.copy()))
                return
            if i >= len(candidates):
                return
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            dfs(i+1, curr, total)
        dfs(0,[],0)
        return f