class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i,j):
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return right - left - 1

        ans = [0,0]

        for each_position in range(len(s)):
            odd_len = check(each_position, each_position)
            if odd_len > (ans[1] - ans[0] + 1):
                dist = odd_len // 2
                ans = [each_position - dist, each_position + dist]
            
            even_len = check(each_position, each_position + 1)
            if even_len > (ans[1] - ans[0] + 1):
                dist = (even_len // 2) - 1
                ans = [each_position - dist, each_position + 1 + dist]
        return s[ans[0]: ans[1]+1]