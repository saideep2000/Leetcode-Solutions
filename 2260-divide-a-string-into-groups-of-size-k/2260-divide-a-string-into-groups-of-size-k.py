class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            if i+k < len(s):
                result.append(s[i:i+k])
                
            else:
                temp = s[i:] + fill*(k-(len(s) - i))
                result.append(temp)
            
            i = i + k
        
        return result