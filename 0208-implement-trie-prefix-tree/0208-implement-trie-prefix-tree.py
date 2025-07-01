class TrieNode():
    def __init__(self):
        self.end = False
        self.children = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        head = self.root
        for each in word:
            if each not in head.children.keys():
                head.children[each] = TrieNode()
            head = head.children[each]
        head.end = True


    def search(self, word: str) -> bool:
        head = self.root
        for each in word:
            if each not in head.children.keys():
                return False
            head = head.children[each]
        if head.end == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for each in prefix:
            if each not in head.children.keys():
                return False
            head = head.children[each]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)