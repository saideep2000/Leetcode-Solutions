class Solution:
    def isValid(self, s: str) -> bool:
        equivalent = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []

        for i in s:
            if i in equivalent.keys():
                stack.append(i)
            else:
                if len(stack) != 0:
                    temp = stack.pop()
                    if temp not in equivalent or equivalent[temp] != i:
                        return False
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False