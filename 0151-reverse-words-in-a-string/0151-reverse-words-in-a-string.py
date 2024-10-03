class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        f = ""
        for i in range(len(l)-1, -1, -1):
            if l[i] != '':
                f = f + l[i] + " "
        f = f[:len(f)-1]
        return f