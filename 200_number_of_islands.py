from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        num = m * n
        parent = [i for i in range(num)]
        size = [1] * num
        count = num
        zero_count = 0

        if num == 0:
            return 0

        def find(p):
            while (p != parent[p]):
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p, q):
            nonlocal count

            root_p = find(p)
            root_q = find(q)

            if root_p == root_q:
                return

            if size[root_p] < size[root_q]:
                parent[root_p] = root_q
                size[root_q] += size[root_p]
            else:
                parent[root_q] = root_p
                size[root_p] += size[root_q]

            count -= 1

            return

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '0':
                    zero_count += 1
                    continue
                # union with neighbors (down, right)
                if i + 1 < m and grid[i + 1][j] == '1':
                    union(i*n + j, (i + 1) * n + j)
                if j + 1 < n and grid[i][j + 1] == '1':
                    union(i*n + j, i*n + j + 1)

        return count - zero_count

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j]:
                    self.dfs(grid, i, j, marked)
                    if grid[i][j] == '1':
                        count += 1

        return count

    def dfs(self, grid, i, j, marked):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or marked[i][j]:
            return

        marked[i][j] = True
        if grid[i][j] == '0':
            return

        self.dfs(grid, i-1, j, marked)
        self.dfs(grid, i+1, j, marked)
        self.dfs(grid, i, j-1, marked)
        self.dfs(grid, i, j+1, marked)


if __name__ == '__main__':
    # given a m x n grid which represent by '1' and '0'
    # return the # of island (island is represented by '1' and surrounded by '0')

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    solution = Solution()
    ans = solution.numIslands(grid)
    assert ans == 3, f'# of islands={ans}'

    ans_dfs = solution.numIslandsDFS(grid)
    assert ans_dfs == 3, f'# of islands={ans_dfs}'
