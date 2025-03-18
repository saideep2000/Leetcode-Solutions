class Solution:
    def rob(self, nums: List[int]) -> int:
        # In -> [11, 50, 100,  2, 2, 100, 11] -> Out
        # In -> [0,   1,   2,  3, 4,   5,  6] -> Out



        # maxRobbedAmount = [None, None, None, None, None, None, None, None]
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]

        # N = 7
        N = len(nums)

        # maxRobbedAmount = [None, None, None, None, None, None, 11, 0]
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        for each in range(N-2, -1, -1):
            maxRobbedAmount[each] = max(maxRobbedAmount[each + 1], maxRobbedAmount[each+2] + nums[each])
        
        return maxRobbedAmount[0]