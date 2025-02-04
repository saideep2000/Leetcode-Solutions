class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = ""
        f_len = 0
        for i in range(0,len(s)):

            # for odd palindromes
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                if f_len-1 < r-l:
                    f = s[l:r+1]
                    f_len = r-l +1
                    print(l,r,f)
                l = l - 1
                r = r + 1

            # for even palindromes
            l,r = i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if f_len-1 < r-l:
                    f = s[l:r+1]
                    f_len = r-l +1
                    print(l,r,f)
                l = l - 1
                r = r + 1
            
        return f
        