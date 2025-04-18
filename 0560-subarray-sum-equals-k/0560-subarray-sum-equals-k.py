class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [1,2,-3,3,-5,8]

        """

        freq = defaultdict(int)
        freq[0] = 1               # sum 0 has occurred once (empty prefix)

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]   # add all prefixes with needed sum
            freq[prefix_sum] += 1           # record this prefix

        return count