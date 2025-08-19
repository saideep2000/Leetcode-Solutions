class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hm = defaultdict(int)
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                hm[mat[i][j]] += 1
        
        result = []

        for key, value in hm.items():
            if value == m:
                result.append(key)
        
        if len(result) == 0:
            return -1 
        
        result.sort()

        return result[0]
