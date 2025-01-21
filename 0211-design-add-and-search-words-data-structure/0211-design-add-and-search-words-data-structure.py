from collections import defaultdict
class Trie():
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        def realSearch(p, trie):
            if p == len(word):
                return trie.end
            if word[p] == ".":
                for i in trie.children:
                    if realSearch(p+1, trie.children[i]):
                        return True
                return False
            if word[p] not in trie.children:
                return False
            else:
                return realSearch(p+1, trie.children[word[p]])

        return realSearch(0, curr)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)