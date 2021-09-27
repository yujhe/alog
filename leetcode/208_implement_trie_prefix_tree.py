class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True, f'apple not found'
    assert trie.search("app") == False, f'app does not exist'
    assert trie.startsWith("app") == True, f'strings with prefix app not found'
    trie.insert("app")
    assert trie.search("app") == True, 'app not found'
