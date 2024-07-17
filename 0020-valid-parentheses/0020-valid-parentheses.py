class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = { "(" : ")" , "{" : "}" , "[" : "]" }
        for i in range(0,len(s)):
            if s[i] in pair.keys():
                stack.append(s[i])
            elif s[i] in pair.values():
                if len(stack):
                    if pair[stack[-1]] != s[i]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True