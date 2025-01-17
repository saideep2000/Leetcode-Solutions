class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        final = derived[0]
        for i in range(1,len(derived)):
            final = final ^ derived[i]
        if final == 0:
            return True
        else:
            return False