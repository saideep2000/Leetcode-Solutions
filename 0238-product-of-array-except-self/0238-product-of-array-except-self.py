class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1]*len(nums)

        for pos in range(1,len(nums)):
            final[pos] = nums[pos-1] * final[pos-1]
        temp = 1
        
        for pos in range(len(nums)-2, -1, -1):
            temp = temp * nums[pos+1]
            final[pos] = final[pos] * temp
            

        return final