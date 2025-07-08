class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        # Use 2D memoization: memo[curr][remaining_events]
        memo = {}
        
        return self.dp(0, events, memo, k)

    def dp(self, curr, events, memo, k):
        # Base cases
        if k == 0 or curr >= len(events):
            return 0
        
        # Check cache
        if (curr, k) in memo:
            return memo[(curr, k)]
        
        # Option 1: Don't include current event
        res = self.dp(curr + 1, events, memo, k)
        
        # Option 2: Include current event
        next_curr = self.binarySearch(curr, events)
        if next_curr != -1:
            res = max(res, events[curr][2] + self.dp(next_curr, events, memo, k - 1))
        else:
            # No next event found, but we can still take current event
            res = max(res, events[curr][2])
        
        memo[(curr, k)] = res
        return res

    def binarySearch(self, curr, events):
        n = len(events)
        left, right = curr + 1, n - 1
        target = events[curr][1]  # End time of current event
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if events[mid][0] > target:  # Start time > end time of current
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result