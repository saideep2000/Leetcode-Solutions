class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = []
        n = len(nums)

        flag = 0
        counter = 0

        for i in range(n):
            if nums[i] == 0:
                if flag == 0:
                    flag = 1

                counter += 1
            else:
                if flag == 1:
                    result.append(counter)
                    flag = 0
                    counter = 0
            
        if flag == 1:
            result.append(counter)
            flag = 0
            counter = 0
    
        final = 0

        for i in range(len(result)):
            each = result[i]
            temp = (each) * (each + 1) // 2
            final = final + temp

        return final
            

