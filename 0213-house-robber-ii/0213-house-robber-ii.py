class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self,arr):
        hm1 = {}
        def dp1(n):
            if n < 0:
                return 0
            if 0 <= n <= 1:
                hm1[n] = arr[n]
                return arr[n]
            ans = 0
            for i in range(0,n-1):
                if i not in hm1:
                    ans = max(ans, dp1(i))
                else:
                    ans = max(ans, hm1[i])
            ans = ans + arr[n]
            hm1[n] = ans
            return ans
        
        n = len(arr)
        return max(dp1(n-1), dp1(n-2))