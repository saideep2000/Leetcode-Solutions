class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        subset = []
        def backtrack(s, subset):
            if len(s) == 1:
                subset.append(s)
                final.append(subset.copy())
                return
            for i in range(0,len(s)):
                combo = subset.copy()
                curr = s[:i+1]
                if curr == curr[::-1]:
                    combo.append(curr)
                    if s[i+1:] != "":
                        backtrack(s[i+1:], combo)
                    else:
                        subset.append(curr)
                        final.append(subset.copy())
                        return
        backtrack(s, subset)
        return final