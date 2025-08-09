class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)      # we'll have the count's of the 0's and 1's 
        q = deque([])   # this will be used for the storing idx of the 0's
        n = len(nums)

        result = 0

        left, right = 0, 0
        while right < n:
            count[nums[right]] = count[nums[right]] + 1

            if nums[right] == 0:
                q.append(right)
            
            if count[0] > k:
                count[0] = count[0] - 1
                oneCount = 0
                dst = q.popleft() + 1
                count[1] = count[1] - (dst-left-1)
                left = dst
                
            
            result = max(result, count[0]+count[1])

            right = right + 1
        
        return result
            