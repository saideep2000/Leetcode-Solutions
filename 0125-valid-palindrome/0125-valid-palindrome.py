class Solution:
    def check_for_alphanum(o):
        if (65 <= o <= 90) or (97 <= o <= 122) or (48 <= o <= 57):
            return False
        else:
            return True
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if Solution.check_for_alphanum(ord(s[i])):
                i = i + 1
            elif Solution.check_for_alphanum(ord(s[j])):
                j = j - 1
            else:
                print(s[i], s[j])
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i = i + 1
                    j = j - 1
        return True

    
