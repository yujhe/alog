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

        print(f'zeros: {zero_count}')

        return count - zero_count


if __name__ == '__main__':
    input = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(f'input: \n' + '\n'.join(' '.join(x) for x in input))
    print(f'output: {Solution().numIslands(input)}')
