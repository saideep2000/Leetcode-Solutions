class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s)-1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i + 1
            j = j - 1
        return s