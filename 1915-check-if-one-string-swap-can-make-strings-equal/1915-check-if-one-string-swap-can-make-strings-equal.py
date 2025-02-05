class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        flag = 0
        temp = -1
        f = 0
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                if flag == 0:
                    temp = i
                    flag = 1
                else:
                    if f == 1:
                        return False
                    if s2[temp] == s1[i] and s2[i] == s1[temp]:
                        f = 1
                    else:
                        return False
        if flag == 1 and f != 1:
            return False
        return True