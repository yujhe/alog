from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board: list[list[int]], i: int, j: int, k: int, word: str) -> bool:
        c = board[i][j]

        if c != word[k]:
            return False

        if k == len(word) - 1:
            return True

        board[i][j] = '#'  # avoid traverse back

        m, n = len(board), len(board[0])
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                if self.dfs(board, x, y, k+1, word):
                    return True

        board[i][j] = c

        return False


if __name__ == '__main__':
    # given an m x n grid of characters board and a string word,
    # return true if word exists in the grid

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    solution = Solution()
    ans = solution.exist(board, word)

    assert ans == True, f'ans={ans}'
