from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # store dictionary in trie data structure
        trie = {}

        for word in dictionary:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['$'] = True

        # replace sentence with shortest root
        replaced = sentence.split()
        for i, word in enumerate(replaced):
            node = trie
            for j, c in enumerate(word):
                if '$' in node:
                    replaced[i] = word[:j]
                    break
                elif c in node:
                    node = node[c]
                else:
                    break

        return ' '.join(replaced)


if __name__ == '__main__':
    # given a dictionary consisting of many roots and
    # a sentence consisting of words separated by spaces,
    # replace all the successors in the sentence with the root forming it.
    # If a successor can be replaced by more than one root,
    # replace it with the root that has the shortest length.
    #
    # Input: dictionary = ["a", "aa", "aaa", "aaaa"],
    # sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    # Output: "a a a a a a a a bbb baba a"

    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"

    solution = Solution()
    ans = solution.replaceWords(dictionary, sentence)

    assert ans == 'the cat was rat by the bat', f'ans={ans}'
