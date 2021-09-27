from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        zero_row, zero_col = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0


if __name__ == '__main__':
    # given a m x n matrix,
    # if the element is 0, set the entire row, column to 0

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    solution = Solution()
    ans = solution.setZeroes(matrix)

    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]], f'ans={matrix}'
