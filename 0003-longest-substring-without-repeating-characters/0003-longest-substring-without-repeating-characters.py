class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rem = collections.defaultdict()
        i, j = 0, 0
        substring = 0
        while j < len(s):
            if s[j] not in rem.keys():
                rem[s[j]] = j
            else:
                i = rem[s[j]] + 1
                j = rem[s[j]]
                rem = collections.defaultdict()
            substring = max(j - i + 1, substring)
            j = j + 1
        return substring
