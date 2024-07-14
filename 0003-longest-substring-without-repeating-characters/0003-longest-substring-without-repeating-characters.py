class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rem = collections.defaultdict()
        i, j = 0, 0
        substring = 0
        substring_len = 0
        while j < len(s):
            if s[j] not in rem.keys():
                rem[s[j]] = j
            else:
                i = rem[s[j]]
                j = rem[s[j]]
                rem = collections.defaultdict()
            substring_len = len(list(rem))
            substring = max(substring_len, substring)
            j = j + 1
            # print()
        return substring
