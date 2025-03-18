class Solution:
    def rob(self, nums: List[int]) -> int:
        # In -> [11, 50, 100,  2, 2, 100, 11] -> Out
        # In -> [0,   1,   2,  3, 4,   5,  6] -> Out

    
        # N = 7
        N = len(nums)

        one, two = 0, nums[N - 1]

        for each in range(N-2, -1, -1):
            temp = max(two, one + nums[each])
            one = two
            two = temp
        
        return two