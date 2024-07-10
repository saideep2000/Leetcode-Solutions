class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_front = ""
        for i in s:
            o = ord(i)
            if o >= 65 and o <= 90:
                s_front = s_front + chr(o+32)
            if o >= 97 and o <= 122:
                s_front = s_front + chr(o)
            if o >= 48 and o <= 57:
                s_front = s_front + chr(o)
        return s_front == s_front[::-1]