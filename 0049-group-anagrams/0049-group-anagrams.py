import collections as cl
class Solution:
    def get_key_by_value(d, value):
        return next((key for key, val in d.items() if val == value), None)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rem = {}
        temp = {}
        for i in strs:
            comp = dict(cl.Counter(i))
            print(comp)
            if comp in rem.values():
                key = Solution.get_key_by_value(rem, comp)
                temp[key].append(i)
            else:
                rem[i] = comp
                temp[i] = [i]
        print(rem)
        print(temp)
        return temp.values()
    