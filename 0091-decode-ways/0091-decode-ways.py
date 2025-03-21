class Solution:
    def numDecodings(self, s: str) -> int:
        hm = defaultdict(int)
        def dfs(decode):
            if len(decode) >= 1 and decode[0] == "0":
                return 0

            if len(decode) == 0:
                return 1
            
            if decode in hm:
                return hm[decode]
            
            temp1, temp2 = 0, 0
            
            # take one digit
            temp1 = dfs(decode[1:])
            
            # take two digits if possible and valid (between 10 and 26)
            if len(decode) >= 2 and 10 <= int(decode[:2]) <= 26:
                temp2 = dfs(decode[2:])
            
            hm[decode] = temp1 + temp2

            return hm[decode]

        return dfs(s)