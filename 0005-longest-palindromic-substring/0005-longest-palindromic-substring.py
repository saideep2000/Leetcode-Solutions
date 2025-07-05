class Solution:
    def longestPalindrome(self, s: str) -> str:
        # so sub-problem is if a single string is palindrome then adding something either side is also a palindrome.
        # a is palindrome then bab is also a palindrome
        # dp(s[start:end]) is palindrome if dp(s[start-1:end:1]) is palindrome and s[start] == s[end]

        # dp[start][end] = (s[start] == s[end]) AND dp[start+1][end-1]

        n = len(s)
        dp = [[None] * n for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i] = True


        
        def check(begin, finish):
            if begin >= finish:
                return True

            if dp[begin][finish] != None:
                return dp[begin][finish]
            
            if s[begin] != s[finish]:
                dp[begin][finish] = False
            else:
                dp[begin][finish] = check(begin+1, finish-1)

            return dp[begin][finish]


        # Check lengths from longest to shortest
        for length in range(n, 0, -1):  # n, n-1, n-2, ..., 1
            for start in range(n - length + 1):
                end = start + length - 1
                if check(start, end):
                    return s[start:end+1]
            
        
        return s[0]

