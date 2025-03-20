class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count = count + 1
                l = l - 1
                r = r + 1
            return count
        total = 0
        for i in range(len(s)):
            odd_count = check(i,i)
            even_count = check(i,i+1)
            total = total + odd_count + even_count
        return total