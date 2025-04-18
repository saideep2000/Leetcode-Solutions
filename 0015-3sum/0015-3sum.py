class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        f = []
        rem = float('inf')
        for k in range(0, len(nums)-2):
            if nums[k] != rem:
                i, j = k+1, len(nums) - 1
                target = nums[k] * -1
                while i<j:
                    if nums[i] + nums[j] == target:
                        f.append([nums[k], nums[i], nums[j]])
                        i = i + 1
                        j = j - 1
                        while i<j and nums[i] == nums[i-1]:
                            i = i + 1
                    # if our number is too big bring down the right pointer down
                    elif nums[i] + nums[j] > target:
                        j = j - 1
                    # or else bring the left one
                    else:
                        i = i + 1
            rem = nums[k]
        return f