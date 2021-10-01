from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # store words in trie data structure
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['$'] = True

        # check all characters on the board
        find = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    self.dfs(board, i, j, trie, find, '')

        return find

    def dfs(self, board: list[list[str]], i: int, j: int, trie: dict, find: list, prefix: str) -> None:
        c = board[i][j]
        node = trie[c]
        if '$' in node:
            find.append(prefix + c)
            del node['$']

        board[i][j] = '#'  # to avoid duplicate search

        m, n = len(board), len(board[0])
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if x >= 0 and x < m and y >= 0 and y < n and board[x][y] in node:
                self.dfs(board, x, y, node, find, prefix + c)

        board[i][j] = c


if __name__ == '__main__':
    # given a m x n grid of characters and a list of words
    # return all words on the board
    # (the same letter cell can not be used more than onece in a word)

    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    solution = Solution()
    ans = solution.findWords(board, words)

    assert set(ans) == set(["eat", "oath"]), f'ans={ans}'
