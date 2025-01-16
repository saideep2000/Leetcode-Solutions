class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)%2 == 0:
            if len(nums2)%2 == 0:
                return 0
            else:
                xor_1 = nums1[0]
                for i in range(1,len(nums1)):
                    xor_1 = xor_1 ^ nums1[i]
                return xor_1
        else:
            if len(nums2)%2 == 0:
                xor_2 = nums2[0]
                for i in range(1,len(nums2)):
                    xor_2 = xor_2 ^ nums2[i]
                return xor_2
            else:
                xor_1 = nums1[0]
                for i in range(1,len(nums1)):
                    xor_1 = xor_1 ^ nums1[i]
                xor_2 = nums2[0]
                for i in range(1,len(nums2)):
                    xor_2 = xor_2 ^ nums2[i]
                return xor_1^xor_2