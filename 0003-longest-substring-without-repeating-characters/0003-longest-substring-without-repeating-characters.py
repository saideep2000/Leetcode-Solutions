class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 1
        i = 0
        j = i + 1
        # we will have a window from i to j
        while i < len(s) and j <= len(s):
            # print(s[i:j])
            if j == len(s):
                l = max(l, (j-i))
                j = j + 1
            elif s[j] in s[i:j]:
                l = max(l, (j-i))
                # i = i + 1
                # j = i + 1
                while s[i] != s[j]:
                    i = i + 1
                i = i + 1
            else:
                j = j + 1
        return l