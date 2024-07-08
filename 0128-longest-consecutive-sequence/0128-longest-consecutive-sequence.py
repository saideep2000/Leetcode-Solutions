class Solution:
    def rec(rem, i):
        curr = rem[i]
        if i-1 in rem:
            if rem[i-1] == 0:
                rem,curr = Solution.rec(rem,i-1)
            else:
                curr = rem[i-1]
        rem[i] = curr + 1
        return rem,rem[i]
    def longestConsecutive(self, nums: List[int]) -> int:
        rem = {}
        curr = 0
        m = 0
        for i in nums:
            if i not in rem:
                rem[i] = 0
        for i in rem:
            if rem[i] == 0:
                rem,curr = Solution.rec(rem, i)
            if m < curr:
                m = curr
        return m