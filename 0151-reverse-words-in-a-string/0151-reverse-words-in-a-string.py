class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        words = words[::-1]

        while '' in words:
            words.remove('')

        s = " ".join(words)

        return s