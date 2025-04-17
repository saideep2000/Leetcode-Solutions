class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        store_unique = set()
        max_len = 0
        while right < len(s):
            if s[right] in store_unique:
                store_unique.remove(s[left])
                left = left + 1
            else:
                max_len = max(max_len, len(store_unique)+1)
                store_unique.add(s[right])
                right = right + 1
            # print(left,right,store_unique, max_len)
        return max_len