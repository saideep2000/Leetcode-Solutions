class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_robber_i(num):
            n = len(num)
            one, two = 0, num[n-1]
            for i in range(n-2,-1,-1):
                now = max(one + num[i], two)
                one = two
                two = now
            return two

        temp, temp2 = house_robber_i(nums[:len(nums)-1]), house_robber_i(nums[1:len(nums)])
        return max(temp, temp2)

        #  n = 4
        # [2,3,0]
        # [0,1,2,3,4]