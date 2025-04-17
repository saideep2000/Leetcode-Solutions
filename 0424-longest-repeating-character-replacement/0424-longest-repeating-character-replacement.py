class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        """

        def give_me_max(your_store):
            max_store = 0
            for k,v in your_store.items():
                max_store = max(max_store,v)
            return max_store

        store = defaultdict(int)
        left = right = 0
        res = 0
        for right, char in enumerate(s):
            store[char] = store[char] + 1
            curr_max_in_store = give_me_max(store)

            while (right - left + 1) - curr_max_in_store > k:
                store[s[left]] = store[s[left]] - 1
                left = left + 1
            res = max(res,(right - left + 1))

        return res


