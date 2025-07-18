import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # Arrays to store the minimum sum of n elements from left
        # and maximum sum of n elements from right at each position
        left_min = [0] * (2 * n + 1)
        right_max = [0] * (2 * n + 1)
        
        # Calculate minimum sum of n elements from left for each position
        max_heap = []  # For maintaining the n smallest elements (negated for max heap)
        current_sum = 0
        
        # Initialize with first n elements
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
            current_sum += nums[i]
        
        left_min[n] = current_sum
        
        # For positions n+1 to 2n
        for i in range(n, 2 * n):
            # Add current element
            heapq.heappush(max_heap, -nums[i])
            current_sum += nums[i]
            
            # Remove the largest element (smallest in negated max heap)
            largest = -heapq.heappop(max_heap)
            current_sum -= largest
            
            left_min[i + 1] = current_sum
        
        # Calculate maximum sum of n elements from right for each position
        min_heap = []  # For maintaining the n largest elements
        current_sum = 0
        
        # Initialize with last n elements
        for i in range(2 * n, 3 * n):
            heapq.heappush(min_heap, nums[i])
            current_sum += nums[i]
        
        right_max[2 * n] = current_sum
        
        # For positions 2n-1 down to n
        for i in range(2 * n - 1, n - 1, -1):
            # Add current element
            heapq.heappush(min_heap, nums[i])
            current_sum += nums[i]
            
            # Remove the smallest element
            smallest = heapq.heappop(min_heap)
            current_sum -= smallest
            
            right_max[i] = current_sum
        
        # Find minimum difference
        min_diff = float('inf')
        for i in range(n, 2 * n + 1):
            min_diff = min(min_diff, left_min[i] - right_max[i])
        
        return min_diff