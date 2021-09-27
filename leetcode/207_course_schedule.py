from typing import List


class DiGraph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def get_adj(self, v):
        return self.adj[v]


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # to check if there is any cycle in the digraph
        g = DiGraph(numCourses)
        for edge in prerequisites:
            g.add_edge(edge[1], edge[0])

        marked = [-1] * numCourses  # -1: not visited, 0: visiting, 1: visited

        for v in range(numCourses):
            if marked[v] < 0:
                has_cycle = self.dfs(g, v, marked)
                if has_cycle:
                    return False

        return True

    def dfs(self, g: DiGraph, v, marked):
        if marked[v] >= 0:
            return marked[v] == 0

        marked[v] = 0

        for w in g.get_adj(v):
            has_cycle = self.dfs(g, w, marked)
            if has_cycle:
                return True

        marked[v] = 1

        return False


if __name__ == '__main__':
    # given n courses and an array of prerequisites
    # the prerequisites[i] = [a(i), b(i)] which means if you want to take a(i) course you must take b(i) first
    # return true if you can complete all courses else return false
    #
    # Input: numCourses = 2, prerequisites = [[1,0]]
    # Output: true
    # Explanation: There are a total of 2 courses to take.
    # To take course 1 you should have finished course 0. So it is possible.

    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

    solution = Solution()
    ans = solution.canFinish(numCourses, prerequisites)

    assert ans == True, f'ans={ans}'
