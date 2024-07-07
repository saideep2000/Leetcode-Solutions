class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = len(nums)*[0]
        pre = 1
        post = 1
        for i in range(0,len(nums)):
            out[i] = pre
            pre = pre * nums[i]
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * post
            post = post * nums[i]
        return out
        # right_pass = len(nums)*[0]
        # left_pass = len(nums)*[0]
        # out = len(nums)*[0]
        # for i in range(0,len(nums)-1):
        #     if i == 0:
        #         right_pass[i] = nums[i]
        #     else:
        #         right_pass[i] = right_pass[i-1] * nums[i]
        
        # for i in range(len(nums)-1, 0, -1):
        #     print(i)
        #     if i == (len(nums)-1):
        #         left_pass[i] = nums[i]
        #     else:
        #         left_pass[i] = left_pass[i+1] * nums[i]
        # print(right_pass)
        # print(left_pass)
        # for i in range(0,len(nums)):
        #     if i == 0:
        #         out[0] = left_pass[1]
        #     elif i == (len(nums)-1):
        #         out[i] = right_pass[i-1]
        #     else:
        #         out[i] = right_pass[i-1]*left_pass[i+1]
        # return out