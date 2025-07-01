class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 0
        left, right = 0, 0
        while right < len(word):
            if word[left] == word[right]:
                right = right + 1
            else:
                result = result + right - left - 1
                left = right
        result = result + right - left - 1
        return result + 1