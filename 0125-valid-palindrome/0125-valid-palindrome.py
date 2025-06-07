class Solution:
    def check_valid_char(o):
        if (65 <= o <= 90) or (97 <= o <= 122) or (48 <= o <= 57):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i<j:
            if Solution.check_valid_char(ord(s[i])) == False:
                i = i + 1
            elif Solution.check_valid_char(ord(s[j])) == False:
                j = j - 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i = i + 1
                    j = j - 1
        return True