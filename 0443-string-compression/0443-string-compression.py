class Solution:
    def compress(self, chars: List[str]) -> int:
        total = 0
        i,j = 0,0
        curr = 0
        while i < len(chars):
            if i == j :
                total = total + 1
                j = j + 1
            elif j< len(chars) and chars[i] == chars[j]:
                total = total + 1
                j = j + 1
            else:
                if total > 1:
                    chars[curr] = chars[i]
                    temp = str(total)
                    if len(temp) > 1:
                        now = 0
                        while now < len(temp):
                            chars[curr+1] = temp[now]
                            curr = curr+1
                            now = now + 1
                    else:
                        chars[curr+1] = temp
                        curr = curr + 1
                    curr = curr + 1
                else:
                    chars[curr] = chars[i]
                    curr = curr + 1
                i = j
                total = 0
        
        return len(chars[:curr])
