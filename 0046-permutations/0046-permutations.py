class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        def rec(rem):
            if not rem:
                return [[]]
            else:
                per = []
                combo = rec(rem[1:])
                print(rem[0], combo)
                for i in combo:
                    for j in range(0,(len(i)+1)):
                        temp = i[:j] + [rem[0]] + i[j:]
                        per.append(temp)
                return per
        return rec(nums)