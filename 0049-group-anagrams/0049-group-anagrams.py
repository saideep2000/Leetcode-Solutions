class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

    
        def get_key(s):
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)

        

        for each in strs:
            key = get_key(each)
            hm[key].append(each)
        
        return list(hm.values())