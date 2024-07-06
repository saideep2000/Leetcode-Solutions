class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rem = {}
        li = []
        for i in nums:
            if i in rem.keys():
                rem[i] = rem[i] + 1
            else:
                rem[i] = 1
        return [k for k,v in sorted(rem.items(), key=lambda item: item[1], reverse = True)][:k]