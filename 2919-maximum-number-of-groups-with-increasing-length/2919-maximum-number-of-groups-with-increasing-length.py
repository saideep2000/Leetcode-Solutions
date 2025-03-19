class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        # [(count, i)]
        # [(5,2), (2,1), (1, 0)]
        usageLimits.sort()  # sort in non-decreasing order
        total = 0   # prefix sum of usage limits so far
        groups = 0  # count of groups formed
        
        for limit in usageLimits:
            total += limit
            # To form (groups+1) groups, we need at least
            # 1 + 2 + ... + (groups+1) = (groups+1) * (groups+2) // 2 total usages.
            if total >= (groups + 1) * (groups + 2) // 2:
                groups += 1
                
        return groups