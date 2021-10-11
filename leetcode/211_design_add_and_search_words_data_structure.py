class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word)

    def dfs(self, node, word) -> bool:
        for idx, c in enumerate(word):
            if c == '.':
                for v in node:
                    if v != '$' and self.dfs(node[v], word[idx+1:]):
                        return True
                return False
            if c not in node:
                return False
            node = node[c]

        return '$' in node


if __name__ == '__main__':
    # design a data structure that supports adding new words and
    # finding if a string matches any previously added string.

    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')

    assert not wd.search('pad'), f'word `pad` not exist'
    assert wd.search('bad'), f'word `bad` exist'
    assert wd.search('.ad'), f'word `.ad` exist'
    assert wd.search('b..'), f'word `b..` exist'
