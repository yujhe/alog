from typing import List


class MagicDictionary:

    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.trie
            for c in word:
                node = node.setdefault(c, {})
            node['$'] = True

    def search(self, searchWord: str) -> bool:
        '''Returns true if you can change exactly one character in searchWord to
        match any string in the data structure, otherwise returns false.'''

        return self.find(self.trie, searchWord, 0)

    def find(self, node: dict, word: str, changed: int) -> bool:
        if word == '':
            if changed == 1 and '$' in node:
                return True
            else:
                return False

        for v in node:
            if v == '$':
                continue

            if v == word[0]:
                if self.find(node[v], word[1:], changed):
                    return True
            elif changed == 0:  # we change word[0] to v
                if self.find(node[v], word[1:], 1):
                    return True

        return False


if __name__ == '__main__':
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello", "hallo", "leetcode"])
    assert magicDictionary.search("hello") == True, f'`hello` is in in magic dictionary'
    assert magicDictionary.search("hhllo") == True, f'`hhllo` is in magic dictionary'
    assert magicDictionary.search("hell") == False, f'`hell` is not in magic dictionary'
    assert magicDictionary.search("leetcoded") == False, f'`leetcoded` is not in magic dictionary'
