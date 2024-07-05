class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_rem = {}
        for i in s:
            if i not in s_rem.keys():
                s_rem[i] = 1
            else:
                s_rem[i] = s_rem[i] + 1
        temp = len(s_rem)
        print(temp, s_rem)
        for j in t:
            if j not in s_rem:
                return False
            else:
                s_rem[j] = s_rem[j] - 1 
        print(list(s_rem.values()))
        if list(s_rem.values()) != [0]*temp :
            return False
        else:
            return True