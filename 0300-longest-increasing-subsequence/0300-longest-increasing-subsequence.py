class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        memo = {}  # memo[i] = length of LIS starting at index i

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            # Start with length 1 (just nums[i] itself)
            best = 1
            # Try to extend from every j > i
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        # Compute the LIS starting from each index, take the maximum
        max_lis = 0
        for i in range(n):
            max_lis = max(max_lis, dfs(i))

        return max_lis
