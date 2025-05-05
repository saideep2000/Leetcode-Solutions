class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        final_set = set(nums)
        
        longest_seq = 0
        
        # let's itreate through all the numbers
        for each in final_set:
            curr = each
            if curr-1 not in final_set:
                temp_long = 0
                while curr in final_set:
                    temp_long = temp_long + 1
                    curr = curr + 1
                longest_seq = max(longest_seq, temp_long)
        return longest_seq
        
