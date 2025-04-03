class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root
        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]
        node.end = True

    def word_break_dfs(self, s, index, memo):
        if index == len(s):
            return True
        if index in memo:
            return memo[index]
        node = self.root
        for i in range(index, len(s)):
            char = s[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.end:
                if self.word_break_dfs(s, i + 1, memo):
                    memo[index] = True
                    return True
        memo[index] = False
        return False

    # word_break_dfs("leetcode", 0, {})



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert_word(word)
        memo = {}
        res = trie.word_break_dfs(s, 0, memo)
        print(memo)
        return res
