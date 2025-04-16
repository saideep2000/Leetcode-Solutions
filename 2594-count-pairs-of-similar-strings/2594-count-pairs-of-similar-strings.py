import math
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        store = defaultdict(int)
        for i in range(0,len(words)):
            store[frozenset(words[i])] = store[frozenset(words[i])] + 1
        final_count = 0
        for i,j in store.items():
            if j > 1:
                combinations = j * (j - 1) // 2
                final_count = final_count + int(combinations)
        return final_count