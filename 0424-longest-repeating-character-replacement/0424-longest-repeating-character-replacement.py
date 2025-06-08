class Solution:
    def get_the_max(my_dict):
        rem_count = 0
        for i,j in my_dict.items():
            if j > rem_count:
                rem_count = j
        return rem_count

    def characterReplacement(self, s: str, k: int) -> int:
        rem_dict = defaultdict(int)
        i = 0
        long_rep_char_count = 0
        for j in range(0,len(s)):
            rem_dict[s[j]] = rem_dict[s[j]] + 1

            max_char_count = Solution.get_the_max(rem_dict)
            l = j - i + 1
            if l - max_char_count <= k:
                long_rep_char_count = max(long_rep_char_count, l)
            else:
                rem_dict[s[i]] = rem_dict[s[i]] - 1
                i = i + 1
        return long_rep_char_count