class TrieNode():
    def __init__(self):
        self.children = {}
        self.words = []
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, lis, original_str):
        node = self.root
        # ['a', 'e', 't']
        for each in lis:
            if each not in node.children:
                node.children[each] = TrieNode()
            node = node.children[each]
        node.words.append(original_str)
    def collect_words(self):
        lst = []

        def dfs(node):
            if node.words:
                lst.append(node.words)
            for child in node.children.values():
                dfs(child)
            
        dfs(self.root)
        return lst

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trie = Trie()
        for each in strs:
            temp = sorted(each)
            trie.insert(temp, each)
        return trie.collect_words()