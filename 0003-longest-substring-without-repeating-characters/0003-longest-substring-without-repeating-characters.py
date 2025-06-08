class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_count = 0

        start = 0
        rem = {}
        for i in range(len(s)):
            if s[i] in rem.keys():
                temp = rem[s[i]] + 1
                if start < temp:
                    start = temp
            rem[s[i]] = i
            final_count = max(final_count , (i - start + 1))
        return final_count