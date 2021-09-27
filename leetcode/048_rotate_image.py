from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 先轉置矩陣，再翻轉
        self.transpose(matrix)
        self.reverse(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    def reverse(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp


if __name__ == '__main__':
    # given a n x n matrix,
    # rotate the matrix by 90 degree (clockwise)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    solution.rotate(matrix)

    assert matrix == [[7, 4, 1], [8, 5, 2], [
        9, 6, 3]], f'rotated matrix={matrix}'
