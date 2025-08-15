class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # making nums1 to be smaller all the time
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        # let's do binary search on the nums1
        left, right = 0, len(nums1)-1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            nums1Left = nums1[i] if i >= 0 else float(-inf)
            nums2Left = nums2[j] if j >= 0 else float(-inf)
            nums1Right = nums1[i+1] if i+1 < len(nums1) else float(inf)
            nums2Right = nums2[j+1] if j+1 < len(nums2) else float(inf)

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                # odd
                if total % 2 != 0:
                    return min(nums1Right, nums2Right)

                # even
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            
            if nums2Left > nums1Right:
                left = i + 1
            else:
                right = i - 1
            





