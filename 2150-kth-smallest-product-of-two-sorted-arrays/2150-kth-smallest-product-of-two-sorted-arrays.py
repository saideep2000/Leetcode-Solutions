from bisect import bisect, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def check(mid):
            total = 0
            for n1 in nums1:
                if n1 > 0:
                    total += bisect(nums2, mid // n1)
                elif n1 < 0:
                    pos = bisect(nums2, ceil(mid / n1) - 1)
                    total += len(nums2) - pos
                else:
                    if mid >= 0:
                        total += len(nums2)
            return total

        left, right = -10**10 , 10**10 

        while left < right:
            mid = (left + right)//2
            if check(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left