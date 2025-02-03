class Solution:
    def rob(self, nums: List[int]) -> int:
        hm = {}
        def dp(n):
            if n < 0:
                return 0
            if 0 <= n <=1:
                return nums[n]
            ans = 0
            for i in range(0,n-1):
                if i not in hm:
                    ans = max(ans, dp(i))
                else:
                    ans = max(ans, hm[i])
            ans = ans + nums[n]
            hm[n] = ans 
            return ans
        n = len(nums)
        return max(dp(n-1), dp(n-2))