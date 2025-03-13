class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rem = set()
        le = 0
        l = 0
        # expand the window
        for r in range(len(s)):
            while s[r] in rem:
                rem.remove(s[l])
                l = l + 1
            rem.add(s[r])
            le = max(le, (r-l)+1)
        return le