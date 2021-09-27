class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev, cur = 1, 2  # the ways to previous step and current step
        for _ in range(2, n):
            temp = prev
            prev = cur
            cur = temp + cur

        return cur


if __name__ == '__main__':
    # given n staircases,
    # you can climb in 1 or 2 step each time
    # return the # of possible ways to reach the top

    n = 2

    solution = Solution()
    ans = solution.climbStairs(n)

    assert ans == 2, f'ans={ans}'
