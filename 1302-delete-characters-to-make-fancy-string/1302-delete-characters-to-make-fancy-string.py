class Solution:
    def makeFancyString(self, s: str) -> str:
        left, middle, right = 0, 1, 2
        result = ""

        while right < len(s):
            if s[left] != s[middle] or s[middle] != s[right]:
                result = result + s[left]

            left = left + 1
            middle = middle + 1
            right = right + 1
                
        if left < len(s):
            result = result + s[left]
        if middle < len(s):
            result = result + s[middle]

        return result
