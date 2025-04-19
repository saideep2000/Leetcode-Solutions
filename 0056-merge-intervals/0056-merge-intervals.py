class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == [] or len(intervals)==1 :
            return intervals
        
        # we'll sort the list's here
        intervals.sort(key=lambda x: x[0])
    
        result = []
        result.append(intervals[0])
        for i in intervals:
            curr = result.pop()
            print(curr)
            if curr[1] >= i[0]:
                curr[1] = max(curr[1], i[1])
            else:
                result.append(curr)
                curr = i

            result.append(curr)
        return result
