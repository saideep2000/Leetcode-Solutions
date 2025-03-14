class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        rem = defaultdict()
        length = 0
        l = 0
        for r in range(n):
            if s[r] in rem.keys() and rem[s[r]] >= l:
                l = rem[s[r]] + 1
            
            length = max(length, (r-l + 1))
            rem[s[r]] = r
        return length