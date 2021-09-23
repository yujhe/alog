class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we can only move to right or bottom
        # so the possible paths to x[m][n] = x[m-1][n] + x[m][n-1]

        x = [[1]*n]*m

        for i in range(1, m):
            for j in range(1, n):
                x[i][j] = x[i-1][j] + x[i][j-1]

        return x[m-1][n-1]


if __name__ == '__main__':
    # given m x n grid,
    # return the # of possible paths from top-left to bottom-right

    m = 3
    n = 2

    solution = Solution()

    assert solution.uniquePaths(
        m, n) == 3, f'# of possible paths={solution.uniquePaths(m, n)} is incorrect'
