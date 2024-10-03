class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        print(l)
        l.reverse()
        print(l)
        f = ""
        for i in l:
            if i != '':
                f = f + i + " "
        f = f[:len(f)-1]
        return f