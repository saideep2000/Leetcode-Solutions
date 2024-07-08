class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rem = set(nums)
        m = 0
        for i in rem:
            if i-1 in rem:
                continue
            else:
                seq = 0
                while i+seq in rem:
                    seq = seq + 1
                if m < seq:
                    m = seq
        return m
                