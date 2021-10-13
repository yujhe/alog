from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        rs = []

        top, bottom = 0, m-1
        left, right = 0, n-1

        while top < bottom and left < right:
            # top
            for i in range(left, right):
                rs.append(matrix[top][i])
            # right
            for i in range(top, bottom):
                rs.append(matrix[i][right])
            # bottom
            for i in range(right, left, -1):
                rs.append(matrix[bottom][i])
            # left
            for i in range(bottom, top, -1):
                rs.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # iterate remaining 1 x n or m x 1 matrix
        if len(rs) < m*n:
            for i in range(top, bottom+1):
                for j in range(left, right+1):
                    rs.append(matrix[i][j])
        return rs


if __name__ == '__main__':
    # given an m x n matrix,
    # return all elements of the matrix in spiral order

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    solution = Solution()
    ans = solution.spiralOrder(matrix)

    assert ans == [1, 2, 3, 6, 9, 8, 7, 4, 5], f'ans={ans}'
