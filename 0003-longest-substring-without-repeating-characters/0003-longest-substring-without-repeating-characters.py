class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        store_unique = defaultdict(int)
        max_len = 0
        while right < len(s):
            if s[right] in store_unique and store_unique[s[right]] >= left:
                left = store_unique[s[right]] + 1
            else:
                max_len = max(max_len, (right-left+1))
                store_unique[s[right]] = right
                right = right + 1
        return max_len