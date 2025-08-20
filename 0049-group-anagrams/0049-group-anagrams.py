from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, w: str):
        head = self.root
        for ch in sorted(w):
            if ch not in head.children:
                head.children[ch] = TrieNode()
            head = head.children[ch]
        head.word.append(w)

    def get(self):
        result = []
        def dfs(node):
            if node.word:
                result.append(node.word)
            for child in node.children.values():
                dfs(child)
        dfs(self.root)
        return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trie = Trie()
        for s in strs:
            trie.addWord(s)
        return trie.get()
