from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        marked = [False] * len(arr)

        return self.dfs(arr, start, marked)

    def dfs(self, arr, i, marked):
        if i < 0 or i >= len(arr) or marked[i]:
            return False

        marked[i] = True

        if arr[i] == 0:
            return True

        left = i - arr[i]
        right = i + arr[i]

        return self.dfs(arr, left, marked) or self.dfs(arr, right, marked)


if __name__ == '__main__':
    # given an array of non-negative integers and a start position
    # you can jump from the position i to i + arr[i] or i - arr[i]
    # return true if you can reach any index with zero value

    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5

    solution = Solution()

    assert solution.canReach(arr, start) == True
