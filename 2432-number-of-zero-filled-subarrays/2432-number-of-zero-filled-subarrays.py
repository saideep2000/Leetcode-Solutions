class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        result = 0
        for right in range(n):
            if nums[right] != 0:
                left = right + 1
            else:
                result = result + (right - left + 1)

        return result