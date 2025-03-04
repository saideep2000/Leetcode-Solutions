class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        i, j = 0, len(tokens)-1
        m, s = 0, 0
        while i <= j:
            if power >= tokens[i]:
                s = s + 1
                power = power - tokens[i]
                m = max(m,s)
                i = i + 1
            elif s>0:
                s = s - 1
                power = power + tokens[j]
                j = j - 1
            else:
                return m
        return m
