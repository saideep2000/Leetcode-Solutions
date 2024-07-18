class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        res = 0
        l = 0
        for r in range(0,len(s)):
            count[s[r]] = count[s[r]] + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] = count[s[l]] - 1
                l = l + 1
            res = max(res, (r-l+1))
        return res