class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        # looping out all the elements in nums
        for i in range(0,len(nums)):
            if len(stack) == 0:
                stack.append(nums[i])
            elif stack and nums[i] < stack[-1]:
                curr_ele = len(stack)
                till = curr_ele + (len(nums)-i)
                if till > k:
                    while stack and till != k and stack[-1] > nums[i]:
                        stack.pop()
                        till = till - 1
                    stack.append(nums[i])
                elif till <= k:
                    stack.append(nums[i])
                
            elif nums[i] >= stack[-1]:
                if len(stack) < k:
                    stack.append(nums[i])

                
        return stack