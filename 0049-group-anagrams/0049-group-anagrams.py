class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rem = {}
        for i in strs:
            if tuple(sorted(list(i))) in rem.keys():
                rem[tuple(sorted(list(i)))].append(i)
            else:
                rem[tuple(sorted(list(i)))] = [i]
        return rem.values()