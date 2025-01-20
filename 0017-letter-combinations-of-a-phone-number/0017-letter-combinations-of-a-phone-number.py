class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        final = []
        if len(digits) == 0:
            return final
        tele = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(index, subsetStr):
            if index == len(digits):
                final.append(subsetStr)
                return
            curr = tele[digits[index]]
            for i in range(0, len(curr)):
                combo = subsetStr
                combo = combo + curr[i]
                backtrack(index+1, combo)
        backtrack(0, "")
        return final