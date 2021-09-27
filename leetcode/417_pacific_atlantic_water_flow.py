from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # use dfs traversal to find nodes that can connect to 1) top or left  2) right or bottom
        # and find the intersection of nodes that can reach to both side

        m, n = len(heights), len(heights[0])
        # the nodes that can reach to left/top, right/bottom
        left_top_nodes, right_bottom_nodes = set(), set()

        # find nodes that have a path to left/right edge
        for i in range(m):
            self.dfs(heights, i, 0, left_top_nodes)
            self.dfs(heights, i, n-1, right_bottom_nodes)

        # find nodes that have a path to top/bottom edge
        for i in range(n):
            self.dfs(heights, 0, i, left_top_nodes)
            self.dfs(heights, m-1, i, right_bottom_nodes)

        nodes = [list(x) for x in left_top_nodes & right_bottom_nodes]

        return nodes

    def dfs(self, heights, i, j, nodes):
        m, n = len(heights), len(heights[0])

        nodes.add((i, j))

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if x >= 0 and x < m and y >= 0 and y < n:
                if heights[i][j] <= heights[x][y] and (x, y) not in nodes:
                    self.dfs(heights, x, y, nodes)


if __name__ == '__main__':
    # given a m x n retangular island,
    # return nodes that have a path to top/left and right/bottom
    # each node have a integer value, they can connect to other node if the value is larger than the neighbor

    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
        2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    solution = Solution()
    ans = solution.pacificAtlantic(heights)

    assert len(ans) == len(output), f'len(ans)={len(ans)}'
    for x in ans:
        assert x in output, f'{x} is not correct'
