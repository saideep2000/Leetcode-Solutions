class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_front = ""
        s_back = ""
        for i in s:
            o = ord(i)
            if o >= 65 and o <= 90:
                s_front = s_front + chr(o+32)
                s_back = chr(o+32) + s_back
            if o >= 97 and o <= 122:
                s_front = s_front + chr(o)
                s_back = chr(o) + s_back
            if o >= 48 and o <= 57:
                s_front = s_front + chr(o)
                s_back = chr(o) + s_back
        return s_front == s_back