class Solution:
    def rob(self, nums: List[int]) -> int:
    
        # N = 7
        N = len(nums)

        one, two = 0, nums[N - 1]

        for each in range(N-2, -1, -1):
            temp = max(two, one + nums[each])
            one = two
            two = temp
        
        return two