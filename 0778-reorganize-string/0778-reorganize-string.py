from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        store_each_count = Counter(s)
        h = []
        f = ""

        for key in store_each_count:
            h.append((store_each_count[key]*(-1),key))
        
        heapq.heapify(h)

        temp_count, temp_char = heapq.heappop(h)
        f = f + temp_char
        while h:
            curr_count, curr_char = heapq.heappop(h)
            f = f + curr_char

            # Now add the old popped char and mark this one old
            if temp_count + 1 < 0:
                heapq.heappush(h, (temp_count + 1, temp_char))

            temp_count = curr_count
            temp_char = curr_char
        if len(s) != len(f):
            return ""
        
        return f
